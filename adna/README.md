- If you like simplicity, just type: make

- Require
    - AmberTools >= 16
    - pandas: amber.conda install pandas

- If you want to know more
    - How to run this notebook?
    
    ```bash
        $ amber.jupyter notebook notebook.ipynb
    ```
    
    - How to run this notebook remotely?
    
        Check: http://amber-md.github.io/pytraj/latest/tutorials/remote_jupyter_notebook
       
    - How to convert it to HMTL file? There are several ways

        - Open the notebook, run it and choose: File -> Download as -> HTML (.html)
        - Run the command line: 

            ```bash
            amber.jupyter nbconvert --to html pytraj_jupyter_notebook.ipynb
            ```
