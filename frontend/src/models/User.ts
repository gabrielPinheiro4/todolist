import api from "@/axios/axios";


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
}
