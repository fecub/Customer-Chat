<script setup>
import { ref, onMounted, nextTick } from 'vue';
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

const user = ref({ name: '', role: 'customer', id: null });
const chatSession = ref(null);
const messages = ref([]);
const newMessage = ref('');
const pollingInterval = 2000;
let polling = null;
const chatContainer = ref(null);

// Benutzer erstellen
const registerUser = async () => {
  try {
    const response = await axios.post(`${API_BASE_URL}/users/`, {
      name: user.value.name,
      role: user.value.role
    });
    user.value.id = response.data.id;
  } catch (error) {
    console.error("Fehler bei der Registrierung:", error);
  }
};

// Chat starten
const startChat = async () => {
  if (!user.value.id) return alert("Bitte erst registrieren!");
  try {
    const response = await axios.post(`${API_BASE_URL}/chat/chats/`, {
      customer_id: user.value.id,
      customer_name: user.value.name
    });
    chatSession.value = response.data;
    fetchMessages();
    startPolling();
  } catch (error) {
    console.error("Fehler beim Starten des Chats:", error);
  }
};

// Nachricht senden
const sendMessage = async () => {
  if (!newMessage.value.trim()) return;
  try {
    await axios.post(`${API_BASE_URL}/chat/messages/`, {
      chat_id: chatSession.value.id,
      sender_id: user.value.id,
      content: newMessage.value
    });
    newMessage.value = '';
    fetchMessages();
  } catch (error) {
    console.error("Fehler beim Senden der Nachricht:", error);
  }
};

// Nachrichten abrufen
const fetchMessages = async () => {
  if (!chatSession.value) return;
  try {
    const response = await axios.get(`${API_BASE_URL}/chat/chats/${chatSession.value.id}/messages`);
    messages.value = response.data;

    // Warten, bis Vue das DOM aktualisiert hat, dann bis zum ende scrollen
    await nextTick(() => {
      const chatBox = chatContainer.value?.$el;
      if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
      }
    });
  } catch (error) {
    console.error("Fehler beim Abrufen der Nachrichten:", error);
  }
};

// Polling starten (regelmäßige Updates)
const startPolling = () => {
  if (polling) clearInterval(polling);
  polling = setInterval(fetchMessages, pollingInterval);
};

onMounted(() => {
  startPolling();
});
</script>

<template>
  <v-container class="fill-height d-flex flex-column align-center justify-center">
    <v-card class="pa-5" width="400">
      <v-card-title class="text-h5 text-center mb-4">Kundenservice Chat</v-card-title>

      <!-- Benutzerregistrierung -->
      <v-row v-if="!user.id" class="mb-4">
        <v-text-field v-model="user.name" label="Dein Name" outlined dense></v-text-field>
        <v-btn color="primary" block @click="registerUser">Registrieren</v-btn>
      </v-row>

      <!-- Chat starten -->
      <v-row v-if="user.id && !chatSession" class="mb-4">
        <v-btn color="green" block @click="startChat">Chat starten</v-btn>
      </v-row>

      <!-- Chat UI -->
      <v-row v-if="chatSession">
        <v-card elevation="1" class="pa-2" width="100%" height="300">
          <v-card-text ref="chatContainer" class="overflow-auto chat-container">
            <v-container v-for="msg in messages" :key="msg.id"
              :class="msg.sender_id === user.id ? 'text-right' : 'text-left'" class="pa-1">
              <v-chip :color="msg.sender_id === user.id ? 'blue' : 'grey'" class="ma-0">
                {{ msg.content }}
              </v-chip>
            </v-container>
          </v-card-text>
        </v-card>

        <!-- Nachrichteneingabe -->
        <v-row class="mt-2 ml-1 mr-1">
          <v-text-field v-model="newMessage" label="Nachricht..." outlined dense
            @keyup.enter="sendMessage"></v-text-field>
          <v-btn height="70%" color="primary" @click="sendMessage">➤</v-btn>
        </v-row>
      </v-row>
    </v-card>
  </v-container>
</template>

<style>
.chat-container {
  max-height: 250px;
  overflow-y: auto;
}
</style>
