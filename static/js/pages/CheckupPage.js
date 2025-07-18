Vue.component('CheckupPage', {
    template: `
      <section class="feature-page checkup-page">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>🩺 Health Checkups</h2>
  
        <!-- Upcoming Appointments -->
        <div class="checkup-list">
          <div class="checkup-card">
            <div>
              <h3>Blood Pressure Check</h3>
              <p>Dr. Sharma – 22 July, 10:30 AM</p>
            </div>
            <span class="tag is-success">Scheduled</span>
          </div>
  
          <div class="checkup-card">
            <div>
              <h3>Diabetes Screening</h3>
              <p>Dr. Mehta – 25 July, 11:00 AM</p>
            </div>
            <span class="tag is-warning">Upcoming</span>
          </div>
        </div>
  
        <!-- Booking Form (Static for now) -->
        <div class="checkup-form">
          <h3 class="form-heading">📅 Book a Checkup</h3>
  
          <div class="form-group">
            <label>Choose Test</label>
            <select>
              <option>Blood Pressure</option>
              <option>Blood Sugar</option>
              <option>Full Body</option>
              <option>Eye Test</option>
            </select>
          </div>
  
          <div class="form-group">
            <label>Preferred Date</label>
            <input type="date" />
          </div>
  
          <div class="form-group">
            <label>Preferred Time</label>
            <input type="time" />
          </div>
  
          <button class="button is-primary">Book Appointment</button>
        </div>
      </section>
    `
  });