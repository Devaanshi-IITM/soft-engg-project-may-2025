Vue.component('NewsPage', {
    template: `
      <section class="feature-page news-page">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>📰 Latest News</h2>
  
        <div class="news-list">
          <div class="news-card">
            <h3>Senior Health Schemes by Government</h3>
            <p>The government has launched a new program for free annual health checkups for citizens over 60...</p>
            <button class="button is-light is-small">Read More</button>
          </div>
  
          <div class="news-card">
            <h3>Yoga & Wellness for Elders</h3>
            <p>Practicing yoga daily has been shown to reduce anxiety, improve flexibility, and even aid memory retention...</p>
            <button class="button is-light is-small">Read More</button>
          </div>
  
          <div class="news-card">
            <h3>Online Safety for Seniors</h3>
            <p>Learn how to stay safe online, avoid scams, and use technology with confidence. Our quick guide helps you stay secure...</p>
            <button class="button is-light is-small">Read More</button>
          </div>
        </div>
      </section>
    `
  });