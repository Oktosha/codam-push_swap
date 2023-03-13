# codam-push_swap

This repo contains the code for a project at [Codam](https://www.codam.nl/) (School 42 in Amstredam).

To run the code you need:

+ mac machine (should probably work on linux, too, but I haven't tried)
+ C compiler + make to compile the final solution (located in the folder `task`)
+ `checker` binary in the root of the repo for the correctness checks to work
+ C++ compiler to compile and run the prototypes in C++
+ python 3 + plumbum + jupyter + matplotlib + tqdm to be able to run the report notebook

I used `venv` for my python environment. To reproduce it, run:

```bash
python3 -m venv push_swap-env
source push_swap-env/bin/activate
pip install -r requirements.txt
```

After this run:

```bash
jupyter notebook
```

This will start [jupyter notebook](https://jupyter.org/) in your browser. The notebook `report.ipynb` will walk you through the project. Alternatively, you can read the notebook in VSCode or [on github](https://github.com/Oktosha/codam-push_swap/blob/main/report.ipynb).
