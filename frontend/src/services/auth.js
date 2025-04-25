import { UserManager, WebStorageStateStore } from 'oidc-client-ts'

const config = {
  authority: 'http://172.16.1.16:8081/realms/coder', // 請替換為您的 OIDC 提供者網址
  client_id: 'vue', // 請替換為您的客戶端 ID
  redirect_uri: `${window.location.origin}/callback`,
  response_type: 'code',
  scope: 'openid profile email',
  post_logout_redirect_uri: `${window.location.origin}/callback`,
  userStore: new WebStorageStateStore({ store: window.localStorage })
}

class AuthService {
  constructor() {
    this.userManager = new UserManager(config)
    this.user = null
  }

  async login() {
    try {
      await this.userManager.signinRedirect()
    } catch (error) {
      console.error('登入失敗:', error)
      throw error
    }
  }

  async logout() {
    try {
      await this.userManager.signoutRedirect()
    } catch (error) {
      console.error('登出失敗:', error)
      throw error
    }
  }

  async handleRedirect() {
    try {
      await this.userManager.signinRedirectCallback()
    } catch (error) {
      console.error('處理回調時發生錯誤:', error)
    }
  }

  async isAuthenticated() {
    try {
      const user = await this.userManager.getUser()
      return !!user
    } catch (error) {
      return false
    }
  }

  async getUser() {
    try {
      return await this.userManager.getUser()
    } catch (error) {
      return null
    }
  }
}

export const authService = new AuthService()