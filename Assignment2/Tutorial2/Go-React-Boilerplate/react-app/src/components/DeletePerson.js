import React, { Component } from 'react';
import './DeletePerson.css';

class DeletePerson extends Component {
	constructor() {
    super();
    this.state = {
      data: [],
      submitted: false,
      deletekey:{
      	id:0
      },
    }
    this.handleSubmit = this.handleSubmit.bind(this);
    this.getRadioVal;
    
  }


  // Lifecycle hook, runs after component has mounted onto the DOM structure
  componentDidMount() {
    const request = new Request('http://127.0.0.1:8080/people/');
    fetch(request)
      .then(response => response.json())
        .then(data => this.setState({data: data}));
  }
   getRadioVal(form,name){
 	var val;
    var radios = form.elements[name];
    for (var i=0, len=radios.length; i<len; i++) {
        if ( radios[i].checked ) { 
            val = radios[i].value; 
            break;
        }
    }
    return val;
  }


  handleSubmit(event){
  	event.preventDefault();
  	this.state.deletekey.id = this.getRadioVal(document.getElementById('Del'),'form-control');
  	fetch('http://localhost:8080/people/'+this.state.deletekey.id,{
  		method:'DELETE',
  	}).then(response => {
        if(response.status >= 200 && response.status < 300)
  			this.setState({submitted: true});
  	});
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Delete a Person</h1>
        </header>
        <form onSubmit={this.handleSubmit} id="Del">
         <table className="table-hover">
          <thead>
            <tr>
              <th>Delete </th>
              <th>ID</th>
              <th>First Name</th>
              <th>Last Name</th>
              <th>City</th>
            </tr>
          </thead>
          <tbody>{this.state.data.map(function(item, key) {
               return (
                  <tr key = {key}>
                  	  <td><input type="radio" name="form-control" value = {item.id} /> </td>
                      <td>{item.id}</td>
                      <td>{item.firstname}</td>
                      <td>{item.lastname}</td>
                      <td>{item.city}</td>
                  </tr>
                )
             })}
          </tbody>
       </table>
       <br/>
       {this.state.submitted &&
          <div>
            <h4>
              Deleting Person with key {this.state.deletekey.id} refesh to see the change.
            </h4>
          </div>
        }
       <button type="submit" className="btn btn-default">Submit</button>
       </form>

       
       
       
      </div>
    );
  }
}

export default DeletePerson;
