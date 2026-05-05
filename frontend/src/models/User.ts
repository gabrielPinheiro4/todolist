import api from "@/axios/axios";
import Cookies from 'js-cookie'

import { checkType } from "@/utils/check";
import type { UserInterface } from "@/types/env";


export default class User {

  name: string;
  passwd: string;
  email: string;

  constructor(name: string, passwd: string, email: string) {
    this.name = name;
    this.passwd = passwd;
    this.email = email;
  }

  async cadUser() {

    try {

      const res = await api.post('/users', {
        name: this.name, passwd: this.passwd, email: this.email
      });

      if (res.status == 200) {

        if (typeof res.data ==  'string') return res.data;
      }

      return null;

    } catch(error) {
      throw error;
    }

  }

  static async login(email: string, passwd: string) {

    try {

      await api.post('/login',
        { email, passwd },
        { withCredentials: true }
      );

    } catch (error) {
      throw error;
    }
  }

  static async getUser() {

    const jwt = Cookies.get('csrf_access_token');

    if (jwt) {

      const res = await api.get('users', {
        headers: { 'X-CSRF-TOKEN': jwt },
        withCredentials: true
      });

      if (checkType<UserInterface>(res.data, 'email')) {

        return res.data
      }
    }

    return null;

  }
}
