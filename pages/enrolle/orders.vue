<template>
  <block-ab title="Приказы о зачислении" class="enrollment-orders">
    <common-documents-list json-path="documents/enrolle-orders.json" class="documents-list" />

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

.notice-container {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-top: 1.5rem;
}

.notice-text {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #34495e;
  margin-bottom: 1rem;

  strong {
    color: #e74c3c;
    font-weight: 600;
  }
}

.highlight {
  background-color: #fff9e6;
  padding: 12px 15px;
  border-left: 4px solid #f1c40f;
  border-radius: 0 4px 4px 0;
  font-weight: 500;
  color: #2c3e50;
}

@media (max-width: 768px) {
  .enrollment-orders {
    padding: 15px;
  }

  ::v-deep .block-ab__title {
    font-size: 1.5rem;
  }

  .notice-text {
    font-size: 1rem;
  }
}
</style>
