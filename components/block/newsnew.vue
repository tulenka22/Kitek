<!-- <template>
  <div class="wrapper">

    <div class="news">
      <h2 class="block-title">Новости</h2>

      <div class="news-card" v-for="item in news" :key="item.id">
        <img :src="item.image" class="news-img" />

        <div class="news-content">
          <h3>{{ item.title }}</h3>
          <p class="date">{{ item.date }}</p>
          <p>{{ item.description }}</p>

          <button class="btn">Читать далее →</button>
        </div>
      </div>
    </div>

    <div class="events">
      <h2 class="block-title">События</h2>

      <div class="event-card" v-for="event in events" :key="event.id">
        <h4>{{ event.title }}</h4>
        <p>{{ event.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import news from '@/data/news.json'
import events from '@/data/events.json'

export default {
  name: 'NewsEvents',

  data() {
    return {
      news,
      events,
    }
  },
}
</script>

<style scoped>
.wrapper {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
  padding: 30px;
}

/* заголовки */
.block-title {
  border-left: 6px solid #c62828;
  padding-left: 12px;
  color: #c62828;
  margin-bottom: 20px;
}

/* НОВОСТИ */
.news-card {
  display: flex;
  gap: 20px;
  background: #f5f5f5;
  border-radius: 14px;
  padding: 15px;
  margin-bottom: 20px;
  transition: 0.3s;
}

.news-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.news-img {
  width: 260px;
  height: 180px;
  object-fit: cover;
  border-radius: 10px;
}

.news-content h3 {
  margin: 0;
  color: #2c3e50;
}

.date {
  font-size: 14px;
  color: #888;
}

.btn {
  margin-top: 10px;
  padding: 8px 14px;
  background: #c62828;
  border: none;
  color: white;
  border-radius: 8px;
  cursor: pointer;
}

/* СОБЫТИЯ */
.event-card {
  background: #f5f5f5;
  border-radius: 12px;
  padding: 15px;
  margin-bottom: 15px;
  transition: 0.3s;
}

.event-card:hover {
  background: #eee;
}

/* адаптив */
@media (max-width: 900px) {
  .wrapper {
    grid-template-columns: 1fr;
  }

  .news-card {
    flex-direction: column;
  }

  .news-img {
    width: 100%;
  }
}
</style> -->
