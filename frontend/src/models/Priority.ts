import Cookies from 'js-cookie'
import api from "@/axios/axios";

import { checkType } from '@/utils/check';
import type { StatusPriorityInterface } from '@/types/env';


export default class Priority {

  static async getPriorities () {

    const jwt = Cookies.get('csrf_access_token');

    if (jwt) {

      const res = await api.get('/priorities', {
        headers: { 'X-CSRF-TOKEN': jwt }, withCredentials: true
      });

      if (res.data instanceof Array) {

        if (
          res.data.every(
            item => checkType<StatusPriorityInterface>(item, 'title')
          )
        )
        {
          return res.data;
        }
      }

    }

    return null;

  }
}
