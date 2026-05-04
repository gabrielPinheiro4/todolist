import { defineStore } from "pinia";


export const useUserStore = defineStore('user', () => {

  const userLoggedIn = () => {
    return document.cookie.includes('csrf_access_token');
  }

  return {
    userLoggedIn,
  }

});
