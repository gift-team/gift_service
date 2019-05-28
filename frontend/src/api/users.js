import {HTTP} from './common'

export const Users = {
  create (config) {
    return HTTP.post('/auth/register/', config).then(response => {
      return response.data
    })
  },
  delete (user) {
    return HTTP.delete(`/auth/users/${user.id}/`)
  },
  list () {
    return HTTP.get('/auth/users').then(response => {
      return response.data
    })
  },
  login (config) {
    return HTTP.post('auth/login/', config).then(response => {
      return response.data
    })
  }
}