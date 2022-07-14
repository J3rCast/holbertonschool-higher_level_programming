# 0x0D. SQL - Introduction
<code>0-privileges.sql:</code> <p>Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).</p>
<code>1-create_user.sql:</code> <p>Write a script that creates the MySQL server user user_0d_1.</p>
<ul>
    <li>user_0d_1 should have all privileges on your MySQL server</li>
    <li>The user_0d_1 password should be set to user_0d_1_pwd</li>
    <li>If the user user_0d_1 already exists, your script should not fail</li>
</ul>
<code>2-create_read_user.sql:</code> <p>Write a script that creates the database hbtn_0d_2 and the user user_0d_2.</p>
<ul>
	<li>user_0d_2 should have only SELECT privilege in the database hbtn_0d_2</li>
 	<li>The user_0d_2 password should be set to user_0d_2_pwd</li>
 	<li>If the database hbtn_0d_2 already exists, your script should not fail</li>
 	<li>If the user user_0d_2 already exists, your script should not fail</li>
</ul>
<code>3-force_name.sql:</code> <p>Write a script that creates the table force_name on your MySQL server.</p>
<lu>
	<lu>force_name description:
        	<li>id INT</li>
        	<li>name VARCHAR(256) can’t be null</li>
	</lu>
    	<li>The database name will be passed as an argument of the mysql command</li>
    	<li>If the table force_name already exists, your script should not fail</li>
</lu>


