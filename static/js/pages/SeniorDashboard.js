Vue.component('SeniorDashboard', {
    template: `
      <section class="senior-dashboard">
        <div class="dashboard-header">
          <h2>👋 Welcome, Ramesh ji</h2>
          <router-link to="/" class="logout-button">Logout</router-link>
          <p>Select an option below</p>
        </div>
  
        <div class="dashboard-grid">
          <router-link to="/reminder" class="dashboard-card">
            <i class="fas fa-pills fa-2x"></i>
            <p>Medical Reminder</p>
          </router-link>
          <router-link to="/checkups" class="dashboard-card">
            <i class="fas fa-calendar-check fa-2x"></i>
            <p>Health Checkups</p>
          </router-link>
          <router-link to="/news" class="dashboard-card">
            <i class="fas fa-newspaper fa-2x"></i>
            <p>News</p>
          </router-link>
          <router-link to="/entertainment" class="dashboard-card">
            <i class="fas fa-tv fa-2x"></i>
            <p>Entertainment</p>
          </router-link>
          <router-link to="/bhajans" class="dashboard-card">
            <i class="fas fa-music fa-2x"></i>
            <p>Bhajans & Songs</p>
          </router-link>
          <router-link to="/video-call" class="dashboard-card">
            <i class="fas fa-video fa-2x"></i>
            <p>Video Call Family</p>
          </router-link>
        </div>
  
        <router-link to="/assistant" class="ai-assistant">
          <i class="fas fa-robot"></i>
          <span>AI Assistant</span>
        </router-link>
      </section>
    `
  });