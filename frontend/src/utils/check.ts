export const checkType = <T>(object: unknown, ...keys: Array<keyof T>): object is T => {

  if (object && typeof object == 'object') {

    return keys.every(key => key in object);
  }

  return false;
}
