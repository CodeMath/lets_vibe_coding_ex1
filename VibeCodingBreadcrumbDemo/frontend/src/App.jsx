import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE = 'http://localhost:8000';

function App() {
  const [conversationId, setConversationId] = useState('demo');
  const [content, setContent] = useState('');
  const [breadcrumbs, setBreadcrumbs] = useState([]);

  useEffect(() => {
    fetchConversation();
  }, []);

  const fetchConversation = async () => {
    try {
      const res = await axios.get(`${API_BASE}/breadcrumbs/${conversationId}`);
      setBreadcrumbs(res.data);
    } catch (err) {
      setBreadcrumbs([]);
    }
  };

  const sendMessage = async () => {
    await axios.post(`${API_BASE}/breadcrumbs/`, {
      conversation_id: conversationId,
      step: 1,
      content,
    });
    setContent('');
    fetchConversation();
  };

  return (
    <div>
      <h1>Breadcrumb Demo</h1>
      <input
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Say something"
      />
      <button onClick={sendMessage}>Send</button>
      <ul>
        {breadcrumbs.map((b) => (
          <li key={b.step}>{b.step}: {b.content}</li>
        ))}
      </ul>
    </div>
  );
}
export default App;
