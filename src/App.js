import React from 'react';
import logo from './logo.svg';
import axios from 'axios';
import {Form,Button,Row,Col,Table,ButtonToolbar} from "react-bootstrap";
import './App.css';

let config = {
  headers: {
    "Content-Type": "application/json",
    'Access-Control-Allow-Origin': '*'
  }
}
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      customDomain:'http://panjingping.s3-website-ap-southeast-1.amazonaws.com',
      bucket:'panjingping',
      url:"",
      shortUrl:"",
      urlList:[],
    };

    this.updateInput = this.updateInput.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }


  handleSubmit = event => {
    event.preventDefault();

    const postData = {
      url: this.state.url,
      bucket:this.state.bucket,
      customDomain: this.state.customDomain
    };
     console.log("postData======"+JSON.stringify(postData));
    axios.post(` https://dn27h4k639.execute-api.ap-southeast-1.amazonaws.com/stage1/shorturl/create`, { postData },config)
        .then(res => {
          console.log(res);
          console.log(res.data);
          console.log(res.data.body);
          var response=JSON.parse(res.data.body);

          console.log("url======"+response.short_url);


          this.setState({
            shortUrl: response.short_url
          });


        })
  }
  updateInput(event){
    this.setState({url : event.target.value})
  }

  render() {
    return (
        <div className="App">

          <header className="App-header">
            <Form onSubmit={this.handleSubmit}>
              <Form.Group as={Row} controlId="formHorizontalEmail">
                <Form.Label column sm={2}>
                  URL
                </Form.Label>
                <Col sm={10}>
                  <Form.Control type="url" placeholder="url" onChange={this.updateInput}/>
                </Col>

                <Col sm={{span: 10, offset: 2}}>
                  <Button type="submit">Shorten</Button>
                </Col>

              </Form.Group>

            </Form>

            <a href={this.state.shortUrl}>{this.state.shortUrl}</a>
          </header>
        </div>
    );
  }
}
export default App;
