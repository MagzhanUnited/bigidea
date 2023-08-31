<template>
    <div style="display: flex; flex-direction: column; width: 40%; margin-left: 50dvh">
        <div style="display: flex; flex-direction: row; justify-content: space-between; width: 100%; margin-bottom: 1dvh">
            <span style="font-weight: bold; font-size: 2.5dvh">Сұраныстар</span>
            <div style="display: flex; flex-direction: row">
                <Button icon="pi pi-pencil" aria-label="Filter" style="margin-right: 20%; width: 5dvh" />
                <Button icon="pi pi-trash" aria-label="Filter" style="width: 5dvh; color: black" severity="danger" />
            </div>
        </div>
        <div v-if="!isloading" v-for="conversation in conversations">
            <div style="display: flex; flex-direction: row; justify-content: space-between; width: 100%; margin-top: 5%">
                <div style="display: flex; flex-direction: column">
                    <span>{{ conversation.title }}</span>
                    <span>{{ formattedDate(conversation.update_time) }}</span>
                </div>
                <Button icon="pi pi-trash" aria-label="Filter" style="width: 30px; color: black" severity="danger" />
            </div>
            <hr aria-orientation="horizontal" style="margin-top: 3dvh" />
        </div>
        <div v-else>
            <Skeleton height="4rem" style="margin-top: 3%"></Skeleton>
            <Skeleton height="4rem" style="margin-top: 3%"></Skeleton>
            <Skeleton height="4rem" style="margin-top: 3%"></Skeleton>
            <Skeleton height="4rem" style="margin-top: 3%"></Skeleton>
            <Skeleton height="4rem" style="margin-top: 3%"></Skeleton>
        </div>
    </div>
</template>
<script>
import { useMainStore } from '../service/composables/userstore';
import moment from 'moment';

export default {
    setup() {
        const nuxtApp = useNuxtApp();
        return { nuxtApp };
    },
    data() {
        return {
            conversations: null,
            inputFormat: 'YYYY-MM-DDTHH:mm:ss.SSSSSSZ',
            outputFormat: 'DD.MM.YYYY HH:mm',
            isloading: true
        };
    },
    async mounted() {
        const response = await this.nuxtApp.$atamekenservice().getConversatinos(useMainStore().get_jwt);
        this.isloading = false;
        this.conversations = response.data;
        console.log('this.conversations:', this.conversations);
    },
    methods: {
        formattedDate(inputDateString) {
            const parsedDate = moment(inputDateString, this.inputFormat);
            return parsedDate.format(this.outputFormat);
        }
    }
};
</script>
<style></style>
