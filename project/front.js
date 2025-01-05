import React, { useState } from 'react';
import axios from 'axios';
import Chart from 'chart.js';

const App = () => {
    const [region, setRegion] = useState('');
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [data, setData] = useState([]);

    const fetchData = async () => {
        const response = await axios.get('/query', {
            params: { region, start_time: startTime, end_time: endTime },
        });
        setData(response.data);
    };

    return (
        <div>
            <h1>Deprem Sorgulama Sistemi</h1>
            <input placeholder="Bölge" onChange={(e) => setRegion(e.target.value)} />
            <input type="date" onChange={(e) => setStartTime(e.target.value)} />
            <input type="date" onChange={(e) => setEndTime(e.target.value)} />
            <button onClick={fetchData}>Sorgula</button>
            <div>
                {/* Chart.js ile görselleştirme */}
            </div>
        </div>
    );
};

export default App;
