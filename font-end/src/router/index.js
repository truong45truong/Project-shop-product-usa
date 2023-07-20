import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import('../views/HomeView.vue')
    },
    {
      path: "/product/:slug",
      name: "detailproduct",
      component: () => import('../views/DetailProductView.vue')
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: '/sign-in',
      name: 'sign-in',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/SignInView.vue')
    },
    {
      path: '/:category',
      name: 'product',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ProductView.vue'),
      meta: {
        requiresAuth: false
      },
      methods: {
        get: true
      }
    },
    {
      path : '/search/:key_search',
      name: 'products-search',
      component: () => import ('../views/ProductSearchView.vue'),
      meta: {
        requiresAuth: false
      },
      methods: {
        get: true
      }
    },
    {
      path : '/checkout/',
      name: 'checkout',
      component: () => import ('../views/CheckoutView.vue'),
      meta: {
        requiresAuth: false
      },
      methods: {
        get: true
      }
    },
    {
      path : '/profile/',
      name: 'profile',
      component: () => import ('../views/InforUserView.vue'),
      meta: {
        requiresAuth: false
      },
      methods: {
        get: true
      }
    },
    {
      path : '/error/',
      name: 'error',
      component: () => import ('../views/ErrorView.vue'),
      meta: {
        requiresAuth: false
      },
      methods: {
        get: true
      }
    },
    {
      path : '/dashboard/',
      name: 'dashboard',
      component: () => import ('../views/DashBoardView.vue'),
      meta: {
        requiresAuth: false
      },
      methods: {
        get: true
      }
    },
  ],
});

export default router;
