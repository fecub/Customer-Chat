<script setup>
import { ref, onMounted, nextTick } from 'vue';
import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000/api';

const supportUser = ref({ id: 999, name: "Support", role: "support" }); // Dummy-Support-ID
const activeChats = ref([]);
const selectedChat = ref(null);
const messages = ref([]);
const newMessage = ref('');
const pollingInterval = 2000;
let polling = null;

// Ref für das Chat-Fenster
const chatContainer = ref(null);

// Aktive Chats abrufen
const fetchActiveChats = async () => {
  try {
    const response = await axios.get(`${API_BASE}/chat/chats/active`);
    activeChats.value = response.data;
  } catch (error) {
    console.error("Fehler beim Laden der aktiven Chats:", error);
  }
};

// Chat auswählen & Nachrichten abrufen
const selectChat = async (chat) => {
  selectedChat.value = chat;
  fetchMessages();
  startPolling();
};

// Nachrichten abrufen
const fetchMessages = async () => {
  if (!selectedChat.value) return;
  try {
    const response = await axios.get(`${API_BASE}/chat/chats/${selectedChat.value.id}/messages`);
    messages.value = response.data;

    // Nach Rendering nach unten scrollen
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

// Nachricht senden
const sendMessage = async () => {
  if (!newMessage.value.trim() || !selectedChat.value) return;
  try {
    await axios.post(`${API_BASE}/chat/messages/`, {
      chat_id: selectedChat.value.id,
      sender_id: supportUser.value.id, // Support sendet
      content: newMessage.value
    });
    newMessage.value = '';
    fetchMessages();
  } catch (error) {
    console.error("Fehler beim Senden der Nachricht:", error);
  }
};

// Polling für Echtzeit-Updates
const startPolling = () => {
  if (polling) clearInterval(polling);
  polling = setInterval(fetchMessages, pollingInterval);
};

onMounted(() => {
  fetchActiveChats();
  setInterval(fetchActiveChats, 5000); // Alle 5s neue Chats laden
});
</script>

<template>
  <v-container class="fill-height d-flex flex-column">
    <v-card class="pa-5" width="600">
      <v-card-title class="text-h5 text-center">Support Chat</v-card-title>

      <!-- Aktive Chats -->
      <v-list>
        <v-list-item v-for="chat in activeChats" :key="chat.id" @click="selectChat(chat)" class="mb-2" dense>
          <v-list-item-title>
            <v-icon class="mr-2">mdi-message</v-icon> Kunde {{ chat.customer_id }}: {{ chat.customer_name }}
          </v-list-item-title>
        </v-list-item>
      </v-list>

      <!-- Chat UI -->
      <v-card v-if="selectedChat" elevation="1" class="pa-2 mt-3" width="100%" height="400">
        <v-card-title class="text-h6">Chat mit Kunde {{ selectedChat.customer_id }}</v-card-title>
        <v-card-text ref="chatContainer" class="overflow-auto chat-container">
          <v-container v-for="msg in messages" :key="msg.id"
            :class="msg.sender_id === supportUser.id ? 'text-right' : 'text-left'" class="pa-1">
            <v-chip :color="msg.sender_id === supportUser.id ? 'blue' : 'grey'" class="ma-1">
              {{ msg.content }}
            </v-chip>
          </v-container>
        </v-card-text>
      </v-card>

      <!-- Nachrichteneingabe -->
      <v-row v-if="selectedChat" class="mt-2 ml-1 mr-1">
        <v-text-field v-model="newMessage" label="Nachricht..." outlined dense
          @keyup.enter="sendMessage"></v-text-field>
        <v-btn height="55" color="primary" @click="sendMessage">➤</v-btn>
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
