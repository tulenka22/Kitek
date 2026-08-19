<template>
  <block-ab title="Приказы о зачислении" class="enrollment-orders">
    <common-documents-list json-path="documents/enrolle-orders.json" class="documents-list" />
    
    <div class="notice-banner-wrapper">
      <div class="notice-banner">
        <span class="notice-banner__text">
          На заочное отделение приём документов продолжается — 
          <strong>успей подать!</strong>
        </span>
      </div>
    </div>
  </block-ab>
</template>

<script>
export default {
  name: 'EnrollmentOrders',
}
</script>

<style scoped lang="scss">
.enrollment-orders {
  padding: 25px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  font-family: 'Roboto', 'Arial', sans-serif;
}

::v-deep .block-ab__title {
  color: #2c3e50;
  text-align: center;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  position: relative;
  padding-bottom: 15px;

  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, #3498db, #2ecc71);
    border-radius: 3px;
  }
}

.documents-list {
  margin: 2rem 0;
}

.notice-banner-wrapper {
  display: flex;
  justify-content: flex-start;
  margin: 1.5rem 0 0.5rem;
}

.notice-banner {
  display: inline-block;
  padding: 8px 16px;
  background-color: #fef9e7;
  border-left: 4px solid #f1c40f;
  border-radius: 4px;
}

.notice-banner__text {
  font-size: 0.95rem;
  line-height: 1.5;
  color: #2c3e50;
  white-space: nowrap;

  strong {
    color: #c0392b;
    font-weight: 600;
  }
}

@media (max-width: 768px) {
  .enrollment-orders {
    padding: 15px;
  }

  ::v-deep .block-ab__title {
    font-size: 1.5rem;
  }

  .notice-banner-wrapper {
    justify-content: flex-start;
  }

  .notice-banner {
    padding: 6px 12px;
  }

  .notice-banner__text {
    font-size: 0.85rem;
    white-space: normal; /* перенос на мобильных */
  }
}
</style>