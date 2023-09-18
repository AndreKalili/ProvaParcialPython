import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="root"
)

cursor = con.cursor()

cursor.execute(
        """ 
                CREATE SCHEMA IF NOT EXISTS `ProvaParcial` DEFAULT CHARACTER SET utf8 ;
USE `ProvaParcial` ;

-- -----------------------------------------------------
-- Table `mydb`.`Department`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProvaParcial`.`Department` (
  `DepartmentId` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(50) NOT NULL,
  `Region` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`DepartmentId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProvaParcial`.`Employee`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `ProvaParcial`.`Employee` (
  `EmployeeId` INT NOT NULL AUTO_INCREMENT,
  `DepartmentId` INT NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `Birthday` DATETIME NOT NULL,
  `Salary` Float(10.2) NOT NULL,
  `Job` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`EmployeeId`),
  INDEX `DepartmentIdx` (`DepartmentId` ASC) VISIBLE,
  CONSTRAINT `DepartmentId`
    FOREIGN KEY (`DepartmentId`)
    REFERENCES `ProvaParcial`.`Department` (`DepartmentId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
"""
    )
print("Tabelas criadas com sucesso.")

cursor.close()
con.close() 

con = mysql.connector.connect(
    host="localhost", database = "ProvaParcial", user="root", password="root"
)

cursor = con.cursor()


def inserir_Department(Name,Region):
    cursor.execute("INSERT INTO Department(Name,Region) VALUES (%s, %s)", (Name, Region))
    print("Departamento inserido com sucesso.")
    con.commit()

def inserir_Employee(DepartmentId,Name,Birthday,Salary,Job):
    cursor.execute("insert into Employee(DepartmentId,Name,Birthday,Salary,Job) VALUES(%s,%s,%s,%s,%s);", (DepartmentId,Name,Birthday,Salary,Job))
    print("Funcionario inserido com sucesso.")
    con.commit()

def listar_Funcionarios_por_Departamento(department_id):
    cursor.execute("SELECT * FROM Employee WHERE DepartmentId = %s", (department_id,))
    Employees = cursor.fetchall()
    if not Employees:
        print("Nenhum funcionário encontrado para o departamento com ID", department_id)
    else:
        print("Funcionários do departamento com ID", department_id, ":")
        for Employee in Employees:
            print(Employee)


def listar_Departments():
    cursor.execute("SELECT * FROM Department")
    Departments = cursor.fetchall()
    if not Departments:
        print("Nenhum departamento encontrado.")
    else:
        print("Departamentos:")
        for Department in Departments:
            print(Department)

def atualizar_Department(DepartmentId, Name, Region):
    cursor.execute(
        "update Department SET Name = %s, Region = %s Where DepartmentId = %s", (Name, Region, DepartmentId)
    )
    print("Departamento atualizado com sucesso.")
    con.commit()

def atualizar_Employee(EmployeeId, Name, Birthday, Salary, Job):
    cursor.execute(
        "update Employee SET Name = %s, Birthday = %s, Salary = %s, Job = %s Where EmployeeId = %s", (Name, Birthday, Salary, Job, EmployeeId)
    )
    print("Funcionario atualizado com sucesso.")
    con.commit()

def deletar_Department(DepartmentId):
    cursor.execute("DELETE FROM Department WHERE DepartmentId = %s", (DepartmentId,))
    print("Departamento deletado com sucesso.")
    con.commit()

def deletar_Employee(EmployeeId):
    cursor.execute("delete from Employee where EmployeeId = %s", (EmployeeId,))
    print("Funcionario deletado com sucesso.")
    con.commit()


    
while True:
    print("\nEscolha uma opção:")
    print("1. Criar um novo departamento")
    print("2. Criar um novo funcionario")
    print("3. Listar um funcionario a partir de um departamento")
    print("4. Listar todos os departamentos")
    print("5. Atualizar um departamento")
    print("6. Atualizar um funcionario")
    print("7. Deletar um funcionario")
    print("8. Deletar um departamento")
    print("9. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        Name = input("Digite o nome do departamento: ")
        Region = input("Digite a região do departamento: ")
        inserir_Department(Name,Region)
   
    elif escolha == "2":
        DepartmentId = int(input("Digite o ID do departamento: "))
        Name = input("Digite o nome do funcionario: ")
        Birthday = input("Digite a data de nascimento do funcionario no seguinte formato AAAA-MM-DD : ")
        Salary = float(input("Digite o salario do funcionario: "))
        Job = input("Digite a funcao do funcionario: ")
        inserir_Employee(DepartmentId,Name,Birthday,Salary,Job)

    elif escolha == "3":
        department_id = input("Digite o ID do departamento para listar os funcionários: ")   
        listar_Funcionarios_por_Departamento(department_id)

    elif escolha == "4":
        listar_Departments()

    elif escolha == "5":
        DepartmentId = int(input("Digite o ID do departamento que deseja atualizar: "))
        Name = input("Digite o novo nome do departamento: ")
        Region = input("Digite a nova região do departamento: ")
        atualizar_Department(DepartmentId, Name, Region)

    elif escolha == "6":
        EmployeeId = int(input("Digite o ID do funcionario que deseja atualizar: "))
        Name = input("Digite o novo nome do funcionario: ")
        Birthday = input("Digite a nova data de nascimento do funcionario: ")
        Salary = float(input("Digite o novo salario do funcionario: "))
        Job = input("Digite a nova funcao do funcionario: ")
        atualizar_Employee(EmployeeId, Name, Birthday, Salary, Job)
    
    elif escolha == "7":
        EmployeeId = int(input("Digite o ID do funcionario que deseja excluir: "))
        deletar_Employee(EmployeeId)
    elif escolha == "8":
        DepartmentId = int(input("Digite o ID do departamento(garanta que nenhum funcionario esteja no deparmento) que deseja excluir: "))
        deletar_Department(DepartmentId)

    elif escolha == "9":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


   
con.close()

print("conectado ao banco de dados MySQL")