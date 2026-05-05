import api from '@/axios/axios';
import type { ProjectInterface } from '@/types/env';
import { checkType } from '@/utils/check';
import Cookies from 'js-cookie'


export default class Project {

  title: string;
  desc: string;

  constructor(title: string, desc: string) {
    this.title = title;
    this.desc = desc;
  }

  async addProject() {

    try {

      const jwt = Cookies.get('csrf_access_token');

      if (jwt) {

        const res = await api.post('/projects', {
          title: this.title,
          desc: this.desc
        }, {
          headers: { 'X-CSRF-TOKEN': jwt },
          withCredentials: true
        });

        if (typeof res.data === 'string') {
          return res.data;
        }
      }

    } catch(error) {
      throw error;
    }
  }

  static async getAllProjects() {

    const jwt = Cookies.get('csrf_access_token');

    if (jwt) {

      const res = await api.get('/projects', {
        headers: { 'X-CSRF-TOKEN': jwt },
        withCredentials: true
      })

      if (res.data instanceof Array) {

        if(res.data.every(item => checkType<ProjectInterface>(item, 'title'))) {
          return res.data;
        }

      }
    }

    return null;
  }
}
