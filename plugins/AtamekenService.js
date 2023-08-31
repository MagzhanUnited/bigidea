import { ATAMEKEN_API, getHeader } from '@/config';
// import { states } from '../service/composables/states';
// import { useMainStore } from '../service/composables/userstore';
// const nuxtApp = useNuxtApp();

// const useMainStore = nuxtApp.$mainstore();
const AtamekenService = {
    // const nuxtApp = useNuxtApp(),
    async askQuestion(prompt, jwt, conv_id) {
        const url = `${ATAMEKEN_API}/ask`;
        console.log('conv_id:', conv_id);
        const response = await useAsyncData(
            'question',
            async () =>
                await $fetch(url, {
                    method: 'POST',
                    body: {
                        prompt: prompt
                        // access_token: states.access_token()
                    },
                    params: {
                        conv_id: conv_id
                    },
                    headers: getHeader(jwt)
                    // headers: {
                    //     'X-CSRF-TOKEN': crsf
                    // }
                })
        );
        console.log('response:', response);
        return response;
    },
    async login(email, password) {
        const url = `${ATAMEKEN_API}/login`;
        const response = await useAsyncData(
            'question',
            async () =>
                await $fetch(url, {
                    method: 'POST',
                    body: {
                        email: email,
                        password: password
                    },
                    headers: getHeader()
                })
        );
        return response;
    },
    async getConversatinos(jwt) {
        console.log('jwt:', jwt);
        const url = `${ATAMEKEN_API}/conversations`;
        const response = await useFetch(url, { method: 'GET', headers: getHeader(jwt) });
        // const response = await useFetch(url, { method: 'GET', headers: getHeader() });
        return response;
    }
};
export default defineNuxtPlugin((nuxtApp) => {
    // Doing something with nuxtApp
    nuxtApp.provide('atamekenservice', () => AtamekenService);
});
