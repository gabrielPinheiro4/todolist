import { defineStore } from "pinia";


export const useUserStore = defineStore('user', () => {

  const getUser = () => {
    return false;
  }

  return {
    getUser,
  }

});
