Vue.component('GuardianAddMusicPage', {
    template: `
      <section class="feature-page guardian-add-music-page">
        <router-link to="/guardiandashboard" class="back-button">← Back</router-link>
        <h2>🎵 Add Music for Parent</h2>
  
        <div class="music-upload-form">
          <div class="field">
            <label class="label">Senior's Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="e.g. Ramesh Kumar" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Track Title</label>
            <div class="control">
              <input class="input" type="text" placeholder="e.g. Om Jai Jagdish" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Artist</label>
            <div class="control">
              <input class="input" type="text" placeholder="e.g. Anuradha Paudwal" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Upload MP3 File</label>
            <div class="control">
              <input class="input" type="file" accept=".mp3" />
            </div>
          </div>
  
          <div class="field has-text-centered">
            <button class="button is-primary">Upload Track</button>
          </div>
        </div>
      </section>
    `
  });