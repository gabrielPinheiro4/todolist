import { defineStore } from "pinia";
import { computed } from "vue";

import User from "@/models/User";

export const useUserStore = defineStore('user', () => {

  const userLoggedIn = () => {
    return document.cookie.includes('csrf_access_token');
  }

  const getUser = computed(async () => await User.getUser());

  return {
    userLoggedIn,
    getUser
  }

});
