Vue.component('GuardianReminderPage', {
    template: `
      <section class="feature-page guardian-reminder-page">
        <router-link to="/guardiandashboard" class="back-button">← Back</router-link>
        <h2>💊 Add Medicine Reminder</h2>
  
        <div class="reminder-form">
          <div class="field">
            <label class="label">Senior's Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="e.g. Ramesh Kumar" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Medicine Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="e.g. Vitamin D3" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Reminder Time</label>
            <div class="control">
              <input class="input" type="time" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Notes</label>
            <div class="control">
              <textarea class="textarea" placeholder="e.g. Take after lunch with warm water"></textarea>
            </div>
          </div>
  
          <div class="field has-text-centered">
            <button class="button is-primary">Set Reminder</button>
          </div>
        </div>
      </section>
    `
  });