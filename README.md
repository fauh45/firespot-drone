# Firespot Drone

To run the program follow the instruction below,

1. Make sure python 3 is installed
2. Create environment to start the code

   ```bash
   python -m venv env
   ```

3. Start the environment

   For windows,

   ```powershell
   .\env\Scripts\activate.bat
   ```

   For linux,

   ```bash
   source env/bin/activate
   ```

   Reference for this part can be seen in [Python docs](https://docs.python.org/3/library/venv.html)

4. Install all the dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Run the edge (drone side) code

   ```bash
   python -m src.edge.main
   ```
