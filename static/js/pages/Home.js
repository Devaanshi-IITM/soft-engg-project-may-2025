Vue.component('Home', {
    template: `
      <div class="main-wrapper">
        <div class="title-bar">
          <h1><img src="/static/assets/mainlogo.png" width="70" height="70"> Saathi</h1>
          <p>Your Digital Companion</p>
        </div>
        <div class="card-glass">
          <h2>Welcome to Saathi</h2>
          <p>Your digital companion for comfort, care and connection</p>
          <div class="button-group">
            <router-link to="/login" class="button login-btn">
              <i class="fas fa-sign-in-alt"></i>&nbsp; Login
            </router-link>
            <router-link to="/register" class="button register-btn">
              <i class="fas fa-user-plus"></i>&nbsp; Register a Senior
            </router-link>
          </div>
        </div>
      </div>
    `
  });