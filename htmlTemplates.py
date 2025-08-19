css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://blog.bismart.com/hs-fs/hubfs/Imported_Blog_Media/los-10-mejores-bots-disponibles-en-Internet-Sep-26-2023-08-53-22-8616-AM.jpg?width=5184&name=los-10-mejores-bots-disponibles-en-Internet-Sep-26-2023-08-53-22-8616-AM.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNxOS7OqEsrsHKwjG7azYC-2M7AOjaP5Blu5xqSfwqdUYAGEAW4JoK2Ak&s">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''