def p_triangle(n_rows):
    rows =[[1]]

    for i in range(1, n_rows):
        row = [1]

        prev_row = rows[i - 1]

        for j in range(1,i):
            row.append(prev_row[j-1] + prev_row[j])

        row.append(1)
        
        rows.append(row)  # Add the current row to the rows list

    return rows  # Return the rows list


print(p_triangle(5))



    
