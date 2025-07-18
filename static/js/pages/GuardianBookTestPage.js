Vue.component('GuardianBookTestPage', {
    template: `
      <section class="feature-page guardian-book-test-page">
        <router-link to="/guardiandashboard" class="back-button">← Back</router-link>
        <h2>🧪 Book Health Test</h2>
  
        <div class="test-booking-form">
          <div class="field">
            <label class="label">Senior's Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="e.g. Sita Devi" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Select Test</label>
            <div class="control">
              <div class="select is-fullwidth">
                <select>
                  <option>Blood Test</option>
                  <option>ECG</option>
                  <option>Diabetes Check</option>
                  <option>Cholesterol Panel</option>
                  <option>Full Body Checkup</option>
                </select>
              </div>
            </div>
          </div>
  
          <div class="field">
            <label class="label">Preferred Date</label>
            <div class="control">
              <input class="input" type="date" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Preferred Time</label>
            <div class="control">
              <input class="input" type="time" />
            </div>
          </div>
  
          <div class="field">
            <label class="label">Additional Notes</label>
            <div class="control">
              <textarea class="textarea" placeholder="e.g. Fasting required before blood test"></textarea>
            </div>
          </div>
  
          <div class="field has-text-centered">
            <button class="button is-success">Book Test</button>
          </div>
        </div>
      </section>
    `
  });