import React from 'react';
import { useState, useEffect } from 'react';
import Avatar from './Avatar';

const API = 'https://dash.dsoou.com/api/comments/';
//const API = 'http://localhost:8000/api/comments/';

function App() {
  const [data, setData] = useState([]);
  const [form, setForm] = useState({});
  const page = window.location.origin + window.location.pathname;
  
  useEffect(() => {
    const fetchData = async() => {
      const res = await fetch(API + '?page=' + page);
      const resJson = await res.json();
      setData(resJson);
    };
    fetchData();
  }, []);

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setForm({...form, [name]:value});
  };

  const handleSubmit = async(e) => {
    e.target.classList.add("is-loading");
    const res = await fetch(API, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ...form,
        title: document.title,
        page: page
      })
    });
    window.location.reload();
  };
  
  return (
    <>
      <hr />
      <h4 className="has-text-weight-bold is-size-4 mb-5">Comments</h4>
      <div className="box">
        <div className="field">
          <label className="label">Email</label>
          <input className="input" type="email" required name="email" value={form.email ? form.email : ""} onChange={handleChange} />
        </div>
        <div className="field">
          <label className="label">Content</label>
          <textarea onChange={handleChange} name="content" className="textarea" required value={form.content ? form.content : ""}></textarea>
        </div>
        <div className="field">
          <button onClick={handleSubmit} className="button is-primary">Submit</button>
        </div>
      </div>
      
      {data.map((row,index) => (
        <div className="media" key={index.toString()}>
          <figure className="media-left">
            <p className="image is-64x64">
              <Avatar email={row.email}/>
            </p>
          </figure>
          <div className="media-content">
            <p className="has-text-weight-bold">{row.email}</p>
            <p>{row.content}</p>
            <p className="has-text-grey">{new Date(row.created_at).toLocaleString()}</p>
          </div>
        </div>
      ))}
    </>
  );
}

export default App;
