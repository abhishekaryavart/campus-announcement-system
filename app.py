from flask import Flask, render_template, request, redirect, url_for, flash, session
from modules.recipient import add_recipient, get_recipients_by_type
from modules.announcement import save_announcement, save_log
from utils.mail_sender import send_email
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-email', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        r_type = request.form.get('type')
        course = request.form.get('course')
        
        add_recipient(name, email, r_type, course)
        flash('Email added successfully!', 'success')
        return redirect(url_for('add_email'))
        
    return render_template('add_email.html')

@app.route('/preview', methods=['POST'])
def preview():
    title = request.form.get('title')
    content = request.form.get('content')
    targets = request.form.getlist('targets')
    
    if not title or not content or not targets:
        flash('Please fill all fields and select at least one target.', 'danger')
        return redirect(url_for('index'))
        
    session['announcement_data'] = {
        'title': title,
        'content': content,
        'targets': targets
    }
    
    return render_template('preview.html', title=title, content=content, targets=targets)

@app.route('/send-announcement', methods=['POST'])
def send_announcement():
    data = session.get('announcement_data')
    if not data:
        flash('No announcement data found. Please try again.', 'danger')
        return redirect(url_for('index'))
        
    title = data['title']
    content = data['content']
    targets = data['targets']
    
    announcement_id = save_announcement(title, content, targets)
    recipients = get_recipients_by_type(targets)
    
    success_count = 0
    fail_count = 0
    
    for r in recipients:
        status = 'Failed'
        if send_email(r['email'], title, content):
            status = 'Sent'
            success_count += 1
        else:
            fail_count += 1
            
        save_log(announcement_id, r['name'], r['email'], r['type'], status)
        
    session.pop('announcement_data', None)
    flash(f'Announcement sent! Success: {success_count}, Failed: {fail_count}', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
