import React, { Component } from 'react';

class Spreadsheet extends React.Component{
	/* ... */
	constructor(props){
		super(props);
	}
	render(){
	var headers = ["Book", "Author", "Language", "Published", "Sales"];
	var data = ["The Lord Of the Rings", "J.R.R. Tolkien", "English", "1954-1955", "150 million"];
	return(<table>
			<thead>
				<tr>
					<th>{headers[0]}</th>
					<th>{headers[1]}</th>
					<th>{headers[2]}</th>
					<th>{headers[3]}</th>
					<th>{headers[4]}</th>
				</tr>
				<tr>
					<th>{data[0]}</th>
					<th>{data[1]}</th>
					<th>{data[2]}</th>
					<th>{data[3]}</th>
					<th>{data[4]}</th>
				</tr>
			</thead>
		</table>);
	}
}

export default Spreadsheet;