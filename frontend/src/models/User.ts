import api from "@/axios/axios";
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

    const res = await api.post('/users', {
      name: this.name, passwd: this.passwd, email: this.email
    });

    console.log(res);

  }
}
