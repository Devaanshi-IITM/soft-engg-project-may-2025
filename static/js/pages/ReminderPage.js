Vue.component('ReminderPage', {
    template: `
      <section class="feature-page medical-reminder">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>💊 Medical Reminders</h2>
  
        <!-- Current Reminders -->
        <div class="reminder-list">
          <div class="reminder-card">
            <div class="pill-info">
              <i class="fas fa-capsules pill-icon"></i>
              <div>
                <h3>Blue Pill</h3>
                <p>8:00 AM – Before Breakfast</p>
              </div>
            </div>
            <span class="status-tag">Daily</span>
          </div>
  
          <div class="reminder-card">
            <div class="pill-info">
              <i class="fas fa-pills pill-icon"></i>
              <div>
                <h3>Vitamin D</h3>
                <p>2:00 PM – After Lunch</p>
              </div>
            </div>
            <span class="status-tag">Weekly</span>
          </div>
  
          <div class="reminder-card">
            <div class="pill-info">
              <i class="fas fa-syringe pill-icon"></i>
              <div>
                <h3>Insulin Shot</h3>
                <p>7:00 PM – After Dinner</p>
              </div>
            </div>
            <span class="status-tag">Daily</span>
          </div>
        </div>
  
        <!-- Add Reminder Button -->
        <div class="add-reminder">
          <button class="button is-primary">
            <i class="fas fa-plus-circle"></i>&nbsp; Add Reminder
          </button>
        </div>
      </section>
    `
  });