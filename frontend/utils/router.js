import AdminDashboard from '../pages/AdminDashboard.js';
import FamilyDashboard from '../pages/FamilyDashboard.js';
import SeniorCitizenDashboard from '../pages/SeniorCitizenDashboard.js';
import NGOsDashboard from '../pages/NGOsDashboard.js';
import GovtDashboard from '../pages/GovtDashboard.js';
import LoginPage from '../pages/LoginPage.js';

// import RegisterPage from '../pages/RegisterPage.js';

const Home = { template: `<div class="container mt-5 text-center"><h1>Welcome to Sathi</h1></div>` };

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: LoginPage },
 
  { path: '/admin', component: AdminDashboard, meta: { requiresAuth: true, role: 'admin' }},
  { path: '/family', component: FamilyDashboard, meta: { requiresAuth: true, role: 'family' }},
  { path: '/senior', component: SeniorCitizenDashboard, meta: { requiresAuth: true, role: 'senior' }},
  { path: '/ngo', component: NGOsDashboard, meta: { requiresAuth: true, role: 'ngo' }},
  { path: '/govt', component: GovtDashboard, meta: { requiresAuth: true, role: 'govt' }}
];

const router = new VueRouter({ routes });
router.beforeEach((to, from, next) => {
  const store = Vue.prototype.$store;
  if (to.meta.requiresAuth && !store.state.loggedIn) return next('/login');
  if (to.meta.role && store.state.role !== to.meta.role) return next('/');
  next();
});
export default router;
