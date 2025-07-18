Vue.component('EntertainmentPage', {
    template: `
      <section class="feature-page entertainment-page">
        <router-link to="/seniordashboard" class="back-button">← Back</router-link>
        <h2>📺 Entertainment & Articles</h2>
  
        <div class="entertainment-grid">
          <div class="entertainment-card">
            <img src="https://placekitten.com/400/200" alt="Story Thumbnail" />
            <h3>Short Story: "The Kind Postman"</h3>
            <p>A heartfelt tale of a retired postman who still delivers joy...</p>
            <button class="button is-link is-small">Read Story</button>
          </div>
  
          <div class="entertainment-card">
            <img src="https://placebear.com/400/200" alt="Video Preview" />
            <h3>Classic Laughter: Johnny Lever</h3>
            <p>A 2-minute laugh riot from the master of comedy.</p>
            <button class="button is-link is-small">Watch Clip</button>
          </div>
  
          <div class="entertainment-card">
            <img src="https://placeimg.com/400/200/nature" alt="Nature" />
            <h3>Tips for Daily Joy</h3>
            <p>Small habits that can brighten your morning routine.</p>
            <button class="button is-link is-small">Explore</button>
          </div>
        </div>
      </section>
    `
  });