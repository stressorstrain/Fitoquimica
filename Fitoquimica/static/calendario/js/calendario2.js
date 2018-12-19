document.getElementById('month-year-nav').innerText= all_months[new Date().getMonth()] + '  '+ new Date().getFullYear();
create_days(new Date().getMonth(), new Date().getFullYear());

function prev0(){
	let current = document.getElementById('month-year-nav').innerText;
	let array = current.split(' ');
	let current_year = array[1];
	let current_month_name = array[0] ;
	let current_prev_month_number = prev_m(current_month_name, current_year);
	let current_prev_year = prev_year(current_year, current_prev_month_number);
	let current_prev_month_name = all_months[current_prev_month_number];
	let table = document.getElementById('main_t');
	let row;
	for(row=2; row<8; row++)
		table.rows[2].remove()
	create_days(current_prev_month_number, current_prev_year);

	document.getElementById('month-year-nav').innerText =current_prev_month_name + ' ' + current_prev_year;
}
function prev_m(current_month_name){
    let prevs_month_number = all_months.indexOf(current_month_name) -1;
     if( prevs_month_number < 0){
        return 11;
		}
	else{
		return prevs_month_number;
		}
	}
function prev_year(year, current_m_number){
    if(current_m_number === 0){
        return year -1;
    }
    else{
        return year;

    }


}
function next_month(){
	let current = document.getElementById('month-year-nav').innerText;
	let array = current.split(' ');
	let current_month_name = array[0] ;
	let current_year = get_year(array[0], array[1]);
	let current_next_month_number = next_n(current_month_name);
	let current_next_month_name = all_months[current_next_month_number];
	let table = document.getElementById('main_t');
	let row;
	for(row=2; row<8; row++){
		table.rows[2].remove()
	}


	create_days(current_next_month_number, current_year);
	document.getElementById('month-year-nav').innerText =current_next_month_name + ' ' + current_year;
}
function get_year(name, year){
	if(name === 'Dezembro'){
		return parseInt(year)+1;
		}
	else{
		return parseInt(year);
		}

	}
function next_n(current_month_name){
	let next = all_months.indexOf(current_month_name)+ 1;
	if(next>11){
		return 0;
		}
	else{
		return next;
		}

	}
function check_bissexto(year) {
    if (year % 4 === 0) {
        return true;
    }
}

function create_days(month, year){
	let week_n  = [0,1,2,3,4];
	let days_n = [0,1,2,3,4,5,6];
	let table = document.getElementById('main_t');
	let tbody = document.getElementById('tbody');
	let prev_month_lenght = prev_month_leng(month, year);
	let curr_month_lenght = month_lenght(all_months[month], year);
	let first_day = first_day_number(year, month);
	let last_days = (last_day_number(year, month, curr_month_lenght));
	let j;
	let i;
	for(i=0; i<=week_n.length; i++){
		let row = document.createElement('tr');
		row.className = 'dia_row';
		row.id = 'tr'+String(i);
		for(j=1; j<=days_n.length; j++){
			let cell = document.createElement('td');
			cell.className = 'dia_cell';
			cell.id = 'cell'+String(j)+String(i);
			cell.innerHTML = null;
			row.appendChild(cell);
		}
		tbody.appendChild(row);
		table.appendChild(tbody);

	}
	insert_days(prev_month_lenght, first_day, tbody, curr_month_lenght, last_days );

	return tbody;

}

function month_lenght(month_name, year){
	if(days_31.includes(month_name)){
		return 31;
		}
	else if(days_30.includes(month_name)){
			return 30;
		}
	else if(days_28.includes(month_name)){
		if(check_bissexto(year) ){
			return 29;
			}
		else{
			return 28;
			}
		}

	}
function prev_month_leng(month, year){
	prev_month = month - 1;
	if(prev_month < 0 ){
		return 31
		}
	else{
		let month_name = all_months[prev_month];
		return  month_lenght(month_name, year )
		}

	}
function first_day_number(year, month){
	return new Date(year, month, 1).getDay();
	}
function last_day_number(year, month, month_len){
	return new Date(year, month, month_len).getDay();
	}

function next(next_number, year){
	let next_month_name = all_months[next_number];
	if(next_number === 11 ){
		let year = full_year_today + 1;
		month_lenght(next_month_name, year);
		}
	else{
		month_lenght(next_month_name, year);
		}
	}
function insert_days(prev_month_lengths, current_first_day_number, table, current_month_lenghts, last_day){
	let x = 0;
	let tb_r = table.rows[2];
	let y = current_first_day_number -1;
	let to_add = current_first_day_number ;
	while(x !== to_add){
		tb_r.cells[x].innerHTML = prev_month_lengths - y;
		tb_r.cells[x].style.color = 'red';
		y = y-1;
		x++;
		}
	tb_r.cells[to_add].innerText = '1';


		let day_count = 1;
		let start = current_first_day_number ;
		let rows;
		let cell;
		if(start > 6){
			start = 0;
			}
		for(rows=2; rows<table.rows.length; rows++){
			if(rows ===2){
				if(day_count <= current_month_lenghts){
					for(cell=start; cell<=6; cell++){
						table.rows[2].cells[cell].innerHTML = String(day_count);
						day_count = day_count +1;
						}
					}
				}


			else {
				for(cell=0; cell<=6; cell++){
					if(day_count <= current_month_lenghts){
						table.rows[rows].cells[cell].innerHTML = String(day_count);
						day_count = day_count +1;
						}
					}
				}
			}
		last_line(last_day, table)
	}
function last_line(last_day, table){
		let row ;
		let cell;

		for(row=5; row<8; row++){
			for(cell=0; cell<7; cell++){
				if(table.rows[row].cells[cell].innerText === ""){
					return insert(row, cell, table)
				}
			}
		}
	}

function insert(first_row, first_null_cell, table){
	let row = table.rows;
	let it;
	let c_inx;
	let nw_rw;
	let count = 1;

	for(it=first_row; it<8; it++){
		for(c_inx=first_null_cell; c_inx<7; c_inx++){
				row[it].cells[c_inx].innerText = String(count);
				row[it].cells[c_inx].style.color = 'red';
				count=count+1;
				first_null_cell = 0;
				nw_rw = true;
			}

		}



	}

