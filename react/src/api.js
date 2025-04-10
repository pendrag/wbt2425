import config from './config';

const apiBaseUrl = config.apiBaseUrl;

export const fetchAvailableBooks = async () => {
  try {
    const response = await fetch(`${apiBaseUrl}/book/available`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching available books:', error);
    throw error;
  }
};
