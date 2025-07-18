Vue.component('VideoCallPage', {
    template: `
      <section class="feature-page video-call-page">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>📹 Video Call Family</h2>
  
        <p class="page-subtext">Tap a family member below to start a call</p>
  
        <div class="family-grid">
          <div class="family-card">
            <img src="https://placehold.co/120x120" alt="Son Avatar" />
            <h3>Aman (Son)</h3>
            <button class="button is-link is-small">
              <i class="fas fa-video"></i>&nbsp; Call Now
            </button>
          </div>
  
          <div class="family-card">
            <img src="https://placehold.co/120x120" alt="Daughter Avatar" />
            <h3>Neha (Daughter)</h3>
            <button class="button is-link is-small">
              <i class="fas fa-video"></i>&nbsp; Call Now
            </button>
          </div>
  
          <div class="family-card">
            <img src="https://placehold.co/120x120" alt="Doctor Avatar" />
            <h3>Dr. Sharma</h3>
            <button class="button is-link is-small">
              <i class="fas fa-video"></i>&nbsp; Call Now
            </button>
          </div>
        </div>
      </section>
    `
  });