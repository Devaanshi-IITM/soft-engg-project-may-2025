Vue.component('GuardianDashboard', {
    template: `
      <section class="dashboard guardian-dashboard">
        <header class="dashboard-header">
          <h2>👨‍👩‍👧 Guardian Dashboard</h2>
          <router-link to="/" class="logout-button">
            <i class="fas fa-sign-out-alt"></i>&nbsp; Logout
          </router-link>
        </header>
  
        <div class="dashboard-grid">
          <router-link to="/guardian/reminder" class="dashboard-card">
            <i class="fas fa-pills"></i>
            <h3>Add Medicine Reminder</h3>
          </router-link>
  
          <router-link to="/guardian/music" class="dashboard-card">
            <i class="fas fa-music"></i>
            <h3>Add Music</h3>
            <p>Upload bhajans or songs for your parent.</p>
          </router-link>
  
          <router-link to="/guardian/checkup" class="dashboard-card">
            <i class="fas fa-stethoscope"></i>
            <h3>Book Health Test</h3>
          </router-link>
        </div>
      </section>
    `
  });