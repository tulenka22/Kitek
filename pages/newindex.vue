<script>
export default {
  data() {
    return {
      specialties: [],
    }
  },
  async created() {
    try {
      const res = await fetch('/documents/education.json')
      this.specialties = await res.json()
    } catch (e) {
      console.error('Ошибка при загрузке JSON:', e)
    }
  },
  computed: {
    specialtesFP() {
      return this.specialties.filter((s) => s.group === 'ФП')
    },
    specialtesOther() {
      return this.specialties.filter((s) => s.group !== 'ФП')
    },
  },
}
</script>

<template>
  <block-ab>
    <section class="education-section">
      <h1 class="education-title">Образование</h1>

      <!-- ФП -->
      <h2 class="education-subtitle">ФП</h2>
      <div v-for="s in specialtesFP" :key="s.id" class="specialty-card">
        <h3 class="specialty-title">{{ s.title }}</h3>
        <p class="specialty-info"><b>Форма обучения:</b> {{ s.formOfEducation }}</p>
        <p class="specialty-info"><b>Срок обучения:</b> {{ s.period }}</p>

        <h4 class="specialty-docs-title">Документы:</h4>
        <ul class="specialty-docs">
          <li v-for="doc in s.documents" :key="doc.url">
            <a :href="doc.url" target="_blank">{{ doc.name }}</a>
          </li>
        </ul>
      </div>

      <!-- Другие специальности -->
      <h2 class="education-subtitle">Другие специальности</h2>
      <div v-for="s in specialtesOther" :key="s.id" class="specialty-card">
        <h3 class="specialty-title">{{ s.title }}</h3>
        <p class="specialty-info"><b>Форма обучения:</b> {{ s.formOfEducation }}</p>
        <p class="specialty-info"><b>Срок обучения:</b> {{ s.period }}</p>

        <h4 class="specialty-docs-title">Документы:</h4>
        <ul class="specialty-docs">
          <li v-for="doc in s.documents" :key="doc.url">
            <a :href="doc.url" target="_blank">{{ doc.name }}</a>
          </li>
        </ul>
      </div>
    </section>
  </block-ab>
</template>

<style scoped>
.education-section {
  max-width: 900px;

  padding: 0 20px;
  font-family: 'Segoe UI', Roboto, sans-serif;
  color: #2c3e50;
}

.education-title {
  font-size: 28px;
  margin-bottom: 25px;
  text-align: left;
}

.education-subtitle {
  font-size: 22px;
  margin: 20px 0 10px;
  color: #1f3a63;
  border-bottom: 1px solid #dcdcdc;
  padding-bottom: 5px;
  text-align: left;
}

.specialty-card {
  background: #ffffff;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  padding: 15px 20px;
  margin-bottom: 20px;
  transition: box-shadow 0.2s;
}

.specialty-card:hover {
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
}

.specialty-title {
  font-size: 18px;
  margin-bottom: 8px;
  color: #1f3a63;
  text-align: left;
}

.specialty-info {
  font-size: 15px;
  margin: 3px 0;
}

.specialty-docs-title {
  margin-top: 12px;
  font-size: 16px;
  color: #1f3a63;
}

.specialty-docs {
  list-style: disc;
  margin: 5px 0 0 20px;
  padding-left: 0;
}

.specialty-docs li {
  margin-bottom: 5px;
}

.specialty-docs a {
  color: #2980b9;
  text-decoration: none;
}

.specialty-docs a:hover {
  text-decoration: underline;
}
</style>
