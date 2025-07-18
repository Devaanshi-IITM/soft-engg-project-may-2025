Vue.component('BhajanPage', {
    template: `
      <section class="feature-page bhajan-page">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>🎶 Bhajans & Songs</h2>
  
        <div class="track-list">
          <div class="track-card">
            <div class="track-info">
              <i class="fas fa-music"></i>
              <div>
                <h3>Raghupati Raghav Raja Ram</h3>
                <p>3:45 mins</p>
              </div>
            </div>
            <audio controls>
              <source src="#" type="audio/mpeg" />
              Your browser does not support the audio element.
            </audio>
          </div>
  
          <div class="track-card">
            <div class="track-info">
              <i class="fas fa-music"></i>
              <div>
                <h3>Vaishnav Jan To</h3>
                <p>4:10 mins</p>
              </div>
            </div>
            <audio controls>
              <source src="#" type="audio/mpeg" />
              Your browser does not support the audio element.
            </audio>
          </div>
  
          <div class="track-card">
            <div class="track-info">
              <i class="fas fa-music"></i>
              <div>
                <h3>Om Jai Jagdish Hare</h3>
                <p>5:00 mins</p>
              </div>
            </div>
            <audio controls>
              <source src="#" type="audio/mpeg" />
              Your browser does not support the audio element.
            </audio>
          </div>
        </div>
      </section>
    `
  });