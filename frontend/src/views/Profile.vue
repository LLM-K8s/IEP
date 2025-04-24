<script setup>
import { ref, onMounted } from 'vue';
import { useKeycloak } from "../plugins/keycloak";

const { keycloak, username } = useKeycloak();
const userInfo = ref({
  email: '',
  firstName: '',
  lastName: '',
  phone: '',
  bio: ''
});

const isEditing = ref(false);
const isLoading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    isLoading.value = true;
    // 確保 Keycloak 已初始化
    if (!keycloak.authenticated) {
      await keycloak.login();
    }

    // 獲取用戶資料
    const userProfile = await keycloak.loadUserProfile();
    console.log('Keycloak user profile:', userProfile); // 用於調試

    userInfo.value = {
      email: userProfile.email || '',
      firstName: userProfile.firstName || '',
      lastName: userProfile.lastName || '',
      phone: userProfile.attributes?.phone?.[0] || '',
      bio: userProfile.attributes?.bio?.[0] || ''
    };
  } catch (err) {
    console.error('獲取用戶資料失敗:', err);
    error.value = '無法獲取用戶資料，請稍後再試';
  } finally {
    isLoading.value = false;
  }
});

const saveProfile = async () => {
  try {
    isLoading.value = true;
    // 更新用戶資料
    await keycloak.updateProfile({
      firstName: userInfo.value.firstName,
      lastName: userInfo.value.lastName,
      email: userInfo.value.email,
      attributes: {
        phone: [userInfo.value.phone],
        bio: [userInfo.value.bio]
      }
    });

    isEditing.value = false;
  } catch (err) {
    console.error('更新個人資料失敗:', err);
    error.value = '更新資料失敗，請稍後再試';
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-100 py-12">
    <div class="max-w-3xl mx-auto bg-white rounded-lg shadow-md p-8">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-2xl font-bold text-gray-800">個人資料</h1>
        <button
          v-if="!isEditing && !isLoading"
          @click="isEditing = true"
          class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        >
          編輯資料
        </button>
      </div>

      <div v-if="isLoading" class="flex justify-center items-center py-8">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
      </div>

      <div v-else-if="error" class="text-red-500 text-center py-4">
        {{ error }}
      </div>

      <div v-else class="space-y-6">
        <div class="grid grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-medium text-gray-700">電子郵件</label>
            <input
              v-if="isEditing"
              v-model="userInfo.email"
              type="email"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
            <p v-else class="mt-1 text-gray-900">{{ userInfo.email }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">電話</label>
            <input
              v-if="isEditing"
              v-model="userInfo.phone"
              type="tel"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
            <p v-else class="mt-1 text-gray-900">{{ userInfo.phone }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">名字</label>
            <input
              v-if="isEditing"
              v-model="userInfo.firstName"
              type="text"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
            <p v-else class="mt-1 text-gray-900">{{ userInfo.firstName }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">姓氏</label>
            <input
              v-if="isEditing"
              v-model="userInfo.lastName"
              type="text"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
            />
            <p v-else class="mt-1 text-gray-900">{{ userInfo.lastName }}</p>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">個人簡介</label>
          <textarea
            v-if="isEditing"
            v-model="userInfo.bio"
            rows="4"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          ></textarea>
          <p v-else class="mt-1 text-gray-900">{{ userInfo.bio }}</p>
        </div>

        <div v-if="isEditing" class="flex justify-end space-x-4">
          <button
            @click="isEditing = false"
            class="px-4 py-2 border border-gray-300 rounded text-gray-700 hover:bg-gray-50 transition-colors"
          >
            取消
          </button>
          <button
            @click="saveProfile"
            class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
          >
            儲存
          </button>
        </div>
      </div>
    </div>
  </div>
</template>