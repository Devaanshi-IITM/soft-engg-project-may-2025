Vue.component('AIAssistantPage', {
    template: `
      <section class="feature-page ai-assistant-page">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>🤖 Sathi AI Assistant</h2>
  
        <!-- Chat Display Area -->
        <div class="chat-box">
          <div class="chat-message user">
            <span>You: What medicine do I take after lunch?</span>
          </div>
          <div class="chat-message assistant">
            <span>Sathi: You have to take the Vitamin D pill at 2:00 PM after lunch.</span>
          </div>
          <div class="chat-message user">
            <span>You: Can you read this prescription?</span>
          </div>
          <div class="chat-message assistant">
            <span>Sathi: Sure! Please hold your phone camera to the paper.</span>
          </div>
        </div>
  
        <!-- Input Area -->
        <div class="chat-input-box">
          <input type="text" placeholder="Ask something..." />
          <button class="button is-primary is-small"><i class="fas fa-paper-plane"></i></button>
          <button class="mic-button"><i class="fas fa-microphone"></i></button>
        </div>
      </section>
    `
  });