from typing import Dict, List
from academics.exam_models import ExamQuestion, ExamChoice

# EXAM_POOLS[major_id][semester] -> List[ExamQuestion]
EXAM_POOLS: Dict[str, Dict[int, List[ExamQuestion]]] = {
    "cs": {
        1: [
            ExamQuestion(
                id="cs_s1_q1",
                text="Which best describes a variable?",
                choices=[
                    ExamChoice(id="a", text="A named storage for data", correct=True),
                    ExamChoice(id="b", text="A type of loop", correct=False),
                    ExamChoice(id="c", text="A database table", correct=False),
                ],
                tags=["python_basics"],
            ),
            ExamQuestion(
                id="cs_s1_q2",
                text="Which construct repeats code while a condition is true?",
                choices=[
                    ExamChoice(id="a", text="if", correct=False),
                    ExamChoice(id="b", text="while", correct=True),
                    ExamChoice(id="c", text="print", correct=False),
                ],
                tags=["control_flow"],
            ),
            ExamQuestion(
                id="cs_s1_q3",
                text="Why do we write functions?",
                choices=[
                    ExamChoice(id="a", text="To reuse and organize logic", correct=True),
                    ExamChoice(id="b", text="To make code longer", correct=False),
                    ExamChoice(id="c", text="To avoid parameters", correct=False),
                ],
                tags=["functions_debug"],
            ),
        ],
        2: [
            ExamQuestion(
                id="cs_s2_q1",
                text="Which data structure follows FIFO?",
                choices=[
                    ExamChoice(id="a", text="Stack", correct=False),
                    ExamChoice(id="b", text="Queue", correct=True),
                    ExamChoice(id="c", text="Tree", correct=False),
                ],
                tags=["ds_linear"],
            ),
            ExamQuestion(
                id="cs_s2_q2",
                text="Average-time complexity of a hash table lookup is usually:",
                choices=[
                    ExamChoice(id="a", text="O(1) amortized", correct=True),
                    ExamChoice(id="b", text="O(n^2)", correct=False),
                    ExamChoice(id="c", text="O(log n) always", correct=False),
                ],
                tags=["hashing_big_o", "big_o"],
            ),
            ExamQuestion(
                id="cs_s2_q3",
                text="What is mathematical induction mainly used for?",
                choices=[
                    ExamChoice(id="a", text="Proving statements over integers", correct=True),
                    ExamChoice(id="b", text="Sorting arrays", correct=False),
                    ExamChoice(id="c", text="Compressing files", correct=False),
                ],
                tags=["logic_proofs"],
            ),
        ],
        3: [
            ExamQuestion(
                id="cs_s3_q1",
                text="Polymorphism in OOP refers to:",
                choices=[
                    ExamChoice(id="a", text="One interface, multiple implementations", correct=True),
                    ExamChoice(id="b", text="Only one class can exist", correct=False),
                ],
                tags=["oop_core"],
            ),
            ExamQuestion(
                id="cs_s3_q2",
                text="Which is closest to what RAM is used for?",
                choices=[
                    ExamChoice(id="a", text="Temporary working memory", correct=True),
                    ExamChoice(id="b", text="Permanent long-term storage", correct=False),
                ],
                tags=["cpu_memory"],
            ),
        ],
        4: [
            ExamQuestion(
                id="cs_s4_q1",
                text="Divide & conquer typically means:",
                choices=[
                    ExamChoice(id="a", text="Split problem, solve subproblems, combine", correct=True),
                    ExamChoice(id="b", text="Try every possibility", correct=False),
                ],
                tags=["divide_conquer"],
            ),
            ExamQuestion(
                id="cs_s4_q2",
                text="A JOIN in SQL is used to:",
                choices=[
                    ExamChoice(id="a", text="Combine rows from two tables using a related column", correct=True),
                    ExamChoice(id="b", text="Delete a table", correct=False),
                ],
                tags=["sql_core"],
            ),
        ],
        5: [
            ExamQuestion(
                id="cs_s5_q1",
                text="A deadlock usually involves:",
                choices=[
                    ExamChoice(id="a", text="Circular wait over resources", correct=True),
                    ExamChoice(id="b", text="A fast CPU", correct=False),
                ],
                tags=["os_scheduling"],
            ),
            ExamQuestion(
                id="cs_s5_q2",
                text="Dynamic programming is best described as:",
                choices=[
                    ExamChoice(id="a", text="Solve subproblems once and reuse results", correct=True),
                    ExamChoice(id="b", text="Always brute force", correct=False),
                ],
                tags=["dynamic_programming"],
            ),
        ],
        6: [
            ExamQuestion(
                id="cs_s6_q1",
                text="TCP is primarily known for:",
                choices=[
                    ExamChoice(id="a", text="Reliable, ordered delivery", correct=True),
                    ExamChoice(id="b", text="Unreliable broadcast", correct=False),
                ],
                tags=["tcp_ip"],
            ),
            ExamQuestion(
                id="cs_s6_q2",
                text="A design pattern is:",
                choices=[
                    ExamChoice(id="a", text="A reusable solution template to a common design problem", correct=True),
                    ExamChoice(id="b", text="A compiler optimization", correct=False),
                ],
                tags=["design_patterns"],
            ),
        ],
        7: [
            ExamQuestion(
                id="cs_s7_q1",
                text="A project milestone is:",
                choices=[
                    ExamChoice(id="a", text="A significant checkpoint in a plan", correct=True),
                    ExamChoice(id="b", text="A random feature", correct=False),
                ],
                tags=["pm_scope"],
            ),
            ExamQuestion(
                id="cs_s7_q2",
                text="A good resume bullet typically includes:",
                choices=[
                    ExamChoice(id="a", text="Impact + metric + action", correct=True),
                    ExamChoice(id="b", text="Only adjectives", correct=False),
                ],
                tags=["resume"],
            ),
        ],
        8: [
            ExamQuestion(
                id="cs_s8_q1",
                text="A post-mortem is used to:",
                choices=[
                    ExamChoice(id="a", text="Learn from what went well and what didn’t after delivery", correct=True),
                    ExamChoice(id="b", text="Avoid documentation", correct=False),
                ],
                tags=["postmortem"],
            ),
            ExamQuestion(
                id="cs_s8_q2",
                text="Deployment testing helps ensure:",
                choices=[
                    ExamChoice(id="a", text="System works reliably in production-like conditions", correct=True),
                    ExamChoice(id="b", text="Faster typing speed", correct=False),
                ],
                tags=["deployment_testing"],
            ),
        ],
    },

    "ba": {
        1: [
            ExamQuestion(
                id="ba_s1_q1",
                text="A balance sheet shows:",
                choices=[
                    ExamChoice(id="a", text="Assets, liabilities, equity at a point in time", correct=True),
                    ExamChoice(id="b", text="Only revenue over a period", correct=False),
                ],
                tags=["acct_balance_sheet"],
            ),
            ExamQuestion(
                id="ba_s1_q2",
                text="Business memos should prioritize:",
                choices=[
                    ExamChoice(id="a", text="Clarity and actionability", correct=True),
                    ExamChoice(id="b", text="Maximum length", correct=False),
                ],
                tags=["biz_writing"],
            ),
        ],
        2: [
            ExamQuestion(
                id="ba_s2_q1",
                text="If demand drops a lot when price increases, demand is:",
                choices=[
                    ExamChoice(id="a", text="Elastic", correct=True),
                    ExamChoice(id="b", text="Inelastic", correct=False),
                ],
                tags=["elasticity"],
            ),
            ExamQuestion(
                id="ba_s2_q2",
                text="Pivot tables are best for:",
                choices=[
                    ExamChoice(id="a", text="Summarizing and analyzing datasets", correct=True),
                    ExamChoice(id="b", text="Encrypting spreadsheets", correct=False),
                ],
                tags=["excel_pivots"],
            ),
        ],
        3: [
            ExamQuestion(
                id="ba_s3_q1",
                text="Time value of money means:",
                choices=[
                    ExamChoice(id="a", text="Money today is worth more than the same amount later", correct=True),
                    ExamChoice(id="b", text="Money never changes value", correct=False),
                ],
                tags=["tvm"],
            ),
            ExamQuestion(
                id="ba_s3_q2",
                text="A bottleneck is:",
                choices=[
                    ExamChoice(id="a", text="The slowest step limiting throughput", correct=True),
                    ExamChoice(id="b", text="A marketing slogan", correct=False),
                ],
                tags=["ops_process"],
            ),
        ],
        4: [
            ExamQuestion(
                id="ba_s4_q1",
                text="Variance analysis compares:",
                choices=[
                    ExamChoice(id="a", text="Budgeted vs actual performance", correct=True),
                    ExamChoice(id="b", text="Only revenue totals", correct=False),
                ],
                tags=["cost_budgeting"],
            ),
            ExamQuestion(
                id="ba_s4_q2",
                text="Regression helps you:",
                choices=[
                    ExamChoice(id="a", text="Estimate relationships between variables", correct=True),
                    ExamChoice(id="b", text="Guarantee profits", correct=False),
                ],
                tags=["regression"],
            ),
        ],
        5: [
            ExamQuestion(
                id="ba_s5_q1",
                text="Competitive forces frameworks are used to:",
                choices=[
                    ExamChoice(id="a", text="Analyze industry attractiveness", correct=True),
                    ExamChoice(id="b", text="Calculate payroll taxes", correct=False),
                ],
                tags=["strategy_frameworks"],
            ),
            ExamQuestion(
                id="ba_s5_q2",
                text="Data storytelling focuses on:",
                choices=[
                    ExamChoice(id="a", text="Clear narrative supported by evidence", correct=True),
                    ExamChoice(id="b", text="As many charts as possible", correct=False),
                ],
                tags=["data_storytelling"],
            ),
        ],
        6: [
            ExamQuestion(
                id="ba_s6_q1",
                text="Scope management helps prevent:",
                choices=[
                    ExamChoice(id="a", text="Scope creep", correct=True),
                    ExamChoice(id="b", text="Team communication", correct=False),
                ],
                tags=["pm_scope"],
            ),
            ExamQuestion(
                id="ba_s6_q2",
                text="Scenario analysis helps you:",
                choices=[
                    ExamChoice(id="a", text="Evaluate outcomes under different assumptions", correct=True),
                    ExamChoice(id="b", text="Avoid budgeting", correct=False),
                ],
                tags=["scenario_analysis"],
            ),
        ],
        7: [
            ExamQuestion(
                id="ba_s7_q1",
                text="A strong pitch typically includes:",
                choices=[
                    ExamChoice(id="a", text="Problem, solution, why now, traction/metrics", correct=True),
                    ExamChoice(id="b", text="Only product features", correct=False),
                ],
                tags=["pitching"],
            ),
            ExamQuestion(
                id="ba_s7_q2",
                text="Case frameworks help you:",
                choices=[
                    ExamChoice(id="a", text="Structure ambiguous business problems", correct=True),
                    ExamChoice(id="b", text="Write software drivers", correct=False),
                ],
                tags=["case_frameworks"],
            ),
        ],
        8: [
            ExamQuestion(
                id="ba_s8_q1",
                text="KPIs are primarily used to:",
                choices=[
                    ExamChoice(id="a", text="Measure performance toward goals", correct=True),
                    ExamChoice(id="b", text="Replace strategy", correct=False),
                ],
                tags=["kpis"],
            ),
            ExamQuestion(
                id="ba_s8_q2",
                text="A post-mortem is useful because it:",
                choices=[
                    ExamChoice(id="a", text="Captures lessons learned for iteration", correct=True),
                    ExamChoice(id="b", text="Eliminates accountability", correct=False),
                ],
                tags=["postmortem"],
            ),
        ],
    },

    # Psychology exams
    "psychology": {
        1: [
            ExamQuestion(
                id="psy_s1_q1",
                text="The field studying behavior and mental processes is:",
                choices=[
                    ExamChoice(id="a", text="Psychology", correct=True),
                    ExamChoice(id="b", text="Philosophy", correct=False),
                    ExamChoice(id="c", text="Neurology", correct=False),
                ],
                tags=["intro_psych"],
            ),
            ExamQuestion(
                id="psy_s1_q2",
                text="Classical conditioning involves learning through:",
                choices=[
                    ExamChoice(id="a", text="Association of stimuli", correct=True),
                    ExamChoice(id="b", text="Punishment only", correct=False),
                    ExamChoice(id="c", text="Introspection", correct=False),
                ],
                tags=["learning_theory"],
            ),
            ExamQuestion(
                id="psy_s1_q3",
                text="The scientific method in psychology requires:",
                choices=[
                    ExamChoice(id="a", text="Testable hypotheses and empirical evidence", correct=True),
                    ExamChoice(id="b", text="Personal opinions only", correct=False),
                    ExamChoice(id="c", text="Intuition alone", correct=False),
                ],
                tags=["research_methods"],
            ),
        ],
        2: [
            ExamQuestion(
                id="psy_s2_q1",
                text="Operant conditioning's key figure is:",
                choices=[
                    ExamChoice(id="a", text="B.F. Skinner", correct=True),
                    ExamChoice(id="b", text="Ivan Pavlov", correct=False),
                    ExamChoice(id="c", text="Albert Bandura", correct=False),
                ],
                tags=["conditioning"],
            ),
            ExamQuestion(
                id="psy_s2_q2",
                text="Memory stages typically include:",
                choices=[
                    ExamChoice(id="a", text="Sensory, short-term, long-term", correct=True),
                    ExamChoice(id="b", text="Fast and slow only", correct=False),
                    ExamChoice(id="c", text="Emotional and logical only", correct=False),
                ],
                tags=["memory_cognition"],
            ),
        ],
        3: [
            ExamQuestion(
                id="psy_s3_q1",
                text="Cognitive biases can lead to:",
                choices=[
                    ExamChoice(id="a", text="Systematic errors in thinking and judgment", correct=True),
                    ExamChoice(id="b", text="Perfect decision-making", correct=False),
                    ExamChoice(id="c", text="Elimination of stress", correct=False),
                ],
                tags=["cognitive_biases"],
            ),
            ExamQuestion(
                id="psy_s3_q2",
                text="Attachment theory focuses on:",
                choices=[
                    ExamChoice(id="a", text="Early parent-child bonds shaping development", correct=True),
                    ExamChoice(id="b", text="Adult career success", correct=False),
                    ExamChoice(id="c", text="Financial planning", correct=False),
                ],
                tags=["development"],
            ),
        ],
        4: [
            ExamQuestion(
                id="psy_s4_q1",
                text="Psychological disorders are typically diagnosed using:",
                choices=[
                    ExamChoice(id="a", text="DSM-5 criteria and clinical assessment", correct=True),
                    ExamChoice(id="b", text="Blood tests only", correct=False),
                    ExamChoice(id="c", text="Random classification", correct=False),
                ],
                tags=["abnormal_psych"],
            ),
            ExamQuestion(
                id="psy_s4_q2",
                text="Cognitive therapy targets:",
                choices=[
                    ExamChoice(id="a", text="Negative thought patterns underlying distress", correct=True),
                    ExamChoice(id="b", text="Physical exercise only", correct=False),
                    ExamChoice(id="c", text="Medication exclusively", correct=False),
                ],
                tags=["therapy"],
            ),
        ],
    },

    # Economics exams
    "economics": {
        1: [
            ExamQuestion(
                id="econ_s1_q1",
                text="Economics is fundamentally about:",
                choices=[
                    ExamChoice(id="a", text="Allocating scarce resources", correct=True),
                    ExamChoice(id="b", text="Making everyone rich", correct=False),
                    ExamChoice(id="c", text="Stock market only", correct=False),
                ],
                tags=["micro_basics"],
            ),
            ExamQuestion(
                id="econ_s1_q2",
                text="Opportunity cost refers to:",
                choices=[
                    ExamChoice(id="a", text="Value of the next best alternative foregone", correct=True),
                    ExamChoice(id="b", text="Price of an opportunity", correct=False),
                    ExamChoice(id="c", text="Cost of advertising", correct=False),
                ],
                tags=["fundamental_concepts"],
            ),
            ExamQuestion(
                id="econ_s1_q3",
                text="Supply and demand equilibrium occurs when:",
                choices=[
                    ExamChoice(id="a", text="Quantity supplied equals quantity demanded", correct=True),
                    ExamChoice(id="b", text="Prices are lowest", correct=False),
                    ExamChoice(id="c", text="Everyone is happy", correct=False),
                ],
                tags=["market_equilibrium"],
            ),
        ],
        2: [
            ExamQuestion(
                id="econ_s2_q1",
                text="Price elasticity of demand measures:",
                choices=[
                    ExamChoice(id="a", text="Responsiveness of quantity demanded to price change", correct=True),
                    ExamChoice(id="b", text="Total revenue always", correct=False),
                    ExamChoice(id="c", text="Supply only", correct=False),
                ],
                tags=["elasticity"],
            ),
            ExamQuestion(
                id="econ_s2_q2",
                text="Comparative advantage explains why countries:",
                choices=[
                    ExamChoice(id="a", text="Specialize and trade to maximize output", correct=True),
                    ExamChoice(id="b", text="Avoid all trade", correct=False),
                    ExamChoice(id="c", text="Produce everything themselves", correct=False),
                ],
                tags=["trade_theory"],
            ),
        ],
        3: [
            ExamQuestion(
                id="econ_s3_q1",
                text="Inflation generally occurs when:",
                choices=[
                    ExamChoice(id="a", text="Money supply grows faster than goods/services", correct=True),
                    ExamChoice(id="b", text="Prices always stay stable", correct=False),
                    ExamChoice(id="c", text="No money exists", correct=False),
                ],
                tags=["macro_money"],
            ),
            ExamQuestion(
                id="econ_s3_q2",
                text="Fiscal policy involves:",
                choices=[
                    ExamChoice(id="a", text="Government spending and taxation", correct=True),
                    ExamChoice(id="b", text="Central bank interest rates only", correct=False),
                    ExamChoice(id="c", text="Corporate dividends", correct=False),
                ],
                tags=["fiscal_policy"],
            ),
        ],
        4: [
            ExamQuestion(
                id="econ_s4_q1",
                text="A budget deficit occurs when:",
                choices=[
                    ExamChoice(id="a", text="Government spending exceeds tax revenue", correct=True),
                    ExamChoice(id="b", text="Unemployment is zero", correct=False),
                    ExamChoice(id="c", text="Interest rates rise", correct=False),
                ],
                tags=["public_finance"],
            ),
            ExamQuestion(
                id="econ_s4_q2",
                text="Behavioral economics studies:",
                choices=[
                    ExamChoice(id="a", text="How psychology affects economic decisions", correct=True),
                    ExamChoice(id="b", text="Only perfectly rational actors", correct=False),
                    ExamChoice(id="c", text="Machines exclusively", correct=False),
                ],
                tags=["behavioral_econ"],
            ),
        ],
    },

    # Political Science exams
    "politics": {
        1: [
            ExamQuestion(
                id="pol_s1_q1",
                text="Political science examines:",
                choices=[
                    ExamChoice(id="a", text="Power, governance, and political systems", correct=True),
                    ExamChoice(id="b", text="Only current news", correct=False),
                    ExamChoice(id="c", text="Historical dates only", correct=False),
                ],
                tags=["intro_polisci"],
            ),
            ExamQuestion(
                id="pol_s1_q2",
                text="Legitimacy in government means:",
                choices=[
                    ExamChoice(id="a", text="Citizens accept authority as rightful", correct=True),
                    ExamChoice(id="b", text="Laws only", correct=False),
                    ExamChoice(id="c", text="Military strength", correct=False),
                ],
                tags=["political_theory"],
            ),
        ],
        2: [
            ExamQuestion(
                id="pol_s2_q1",
                text="A democratic system typically requires:",
                choices=[
                    ExamChoice(id="a", text="Free elections, rule of law, representation", correct=True),
                    ExamChoice(id="b", text="Single leader only", correct=False),
                    ExamChoice(id="c", text="No laws", correct=False),
                ],
                tags=["governance_systems"],
            ),
            ExamQuestion(
                id="pol_s2_q2",
                text="Interest groups try to influence policy through:",
                choices=[
                    ExamChoice(id="a", text="Lobbying, advocacy, coalition-building", correct=True),
                    ExamChoice(id="b", text="Violence only", correct=False),
                    ExamChoice(id="c", text="Ignoring government", correct=False),
                ],
                tags=["interest_groups"],
            ),
        ],
        3: [
            ExamQuestion(
                id="pol_s3_q1",
                text="Foreign policy is shaped by:",
                choices=[
                    ExamChoice(id="a", text="National interests, alliances, international law", correct=True),
                    ExamChoice(id="b", text="Random decisions", correct=False),
                    ExamChoice(id="c", text="One leader's preference only", correct=False),
                ],
                tags=["intl_relations"],
            ),
            ExamQuestion(
                id="pol_s3_q2",
                text="Diplomacy seeks to:",
                choices=[
                    ExamChoice(id="a", text="Resolve conflicts through negotiation", correct=True),
                    ExamChoice(id="b", text="Always declare war", correct=False),
                    ExamChoice(id="c", text="Avoid communication", correct=False),
                ],
                tags=["diplomacy"],
            ),
        ],
    },

    # History exams
    "history": {
        1: [
            ExamQuestion(
                id="hist_s1_q1",
                text="Historical analysis requires examining:",
                choices=[
                    ExamChoice(id="a", text="Primary sources, context, and multiple perspectives", correct=True),
                    ExamChoice(id="b", text="Only textbook versions", correct=False),
                    ExamChoice(id="c", text="One person's opinion", correct=False),
                ],
                tags=["historical_methods"],
            ),
            ExamQuestion(
                id="hist_s1_q2",
                text="Causation in history is typically:",
                choices=[
                    ExamChoice(id="a", text="Complex with multiple contributing factors", correct=True),
                    ExamChoice(id="b", text="Simple and single-cause", correct=False),
                    ExamChoice(id="c", text="Unknowable", correct=False),
                ],
                tags=["causation"],
            ),
        ],
        2: [
            ExamQuestion(
                id="hist_s2_q1",
                text="Primary sources include:",
                choices=[
                    ExamChoice(id="a", text="Original documents, letters, artifacts from the time", correct=True),
                    ExamChoice(id="b", text="Only modern textbooks", correct=False),
                    ExamChoice(id="c", text="Movies only", correct=False),
                ],
                tags=["evidence_interpretation"],
            ),
            ExamQuestion(
                id="hist_s2_q2",
                text="Periodization divides history based on:",
                choices=[
                    ExamChoice(id="a", text="Significant changes in society, culture, politics", correct=True),
                    ExamChoice(id="b", text="Random dates", correct=False),
                    ExamChoice(id="c", text="Individual preferences", correct=False),
                ],
                tags=["periodization"],
            ),
        ],
        3: [
            ExamQuestion(
                id="hist_s3_q1",
                text="Social history examines:",
                choices=[
                    ExamChoice(id="a", text="Everyday lives of ordinary people, families, communities", correct=True),
                    ExamChoice(id="b", text="Only famous leaders", correct=False),
                    ExamChoice(id="c", text="Dates exclusively", correct=False),
                ],
                tags=["social_history"],
            ),
            ExamQuestion(
                id="hist_s3_q2",
                text="Revising historical narratives happens when:",
                choices=[
                    ExamChoice(id="a", text="New evidence emerges or perspectives are included", correct=True),
                    ExamChoice(id="b", text="Historians get bored", correct=False),
                    ExamChoice(id="c", text="Never", correct=False),
                ],
                tags=["historiography"],
            ),
        ],
    },

    # Engineering exams
    "engineering": {
        1: [
            ExamQuestion(
                id="eng_s1_q1",
                text="Engineering design process begins with:",
                choices=[
                    ExamChoice(id="a", text="Defining the problem and requirements", correct=True),
                    ExamChoice(id="b", text="Building immediately", correct=False),
                    ExamChoice(id="c", text="Random construction", correct=False),
                ],
                tags=["design_thinking"],
            ),
            ExamQuestion(
                id="eng_s1_q2",
                text="Stress in materials refers to:",
                choices=[
                    ExamChoice(id="a", text="Force per unit area applied to material", correct=True),
                    ExamChoice(id="b", text="Worker fatigue only", correct=False),
                    ExamChoice(id="c", text="Temperature changes", correct=False),
                ],
                tags=["mechanics_materials"],
            ),
        ],
        2: [
            ExamQuestion(
                id="eng_s2_q1",
                text="Safety factors in design ensure:",
                choices=[
                    ExamChoice(id="a", text="Structure can handle loads beyond expected", correct=True),
                    ExamChoice(id="b", text="Perfect durability forever", correct=False),
                    ExamChoice(id="c", text="No costs", correct=False),
                ],
                tags=["structural_design"],
            ),
            ExamQuestion(
                id="eng_s2_q2",
                text="CAD software is used primarily for:",
                choices=[
                    ExamChoice(id="a", text="Creating precise technical drawings and models", correct=True),
                    ExamChoice(id="b", text="Social media only", correct=False),
                    ExamChoice(id="c", text="Word processing", correct=False),
                ],
                tags=["cad_tools"],
            ),
        ],
    },

    # Biology exams
    "biology": {
        1: [
            ExamQuestion(
                id="bio_s1_q1",
                text="The cell membrane's primary function is:",
                choices=[
                    ExamChoice(id="a", text="Control what enters/exits the cell", correct=True),
                    ExamChoice(id="b", text="Store energy only", correct=False),
                    ExamChoice(id="c", text="Perform photosynthesis", correct=False),
                ],
                tags=["cell_biology"],
            ),
            ExamQuestion(
                id="bio_s1_q2",
                text="DNA carries genetic information in the form of:",
                choices=[
                    ExamChoice(id="a", text="Nucleotide sequences", correct=True),
                    ExamChoice(id="b", text="Proteins only", correct=False),
                    ExamChoice(id="c", text="Sugars exclusively", correct=False),
                ],
                tags=["genetics"],
            ),
        ],
        2: [
            ExamQuestion(
                id="bio_s2_q1",
                text="Photosynthesis converts:",
                choices=[
                    ExamChoice(id="a", text="Light energy into chemical energy (glucose)", correct=True),
                    ExamChoice(id="b", text="Glucose to light", correct=False),
                    ExamChoice(id="c", text="DNA to proteins", correct=False),
                ],
                tags=["plant_physiology"],
            ),
            ExamQuestion(
                id="bio_s2_q2",
                text="Evolution occurs through:",
                choices=[
                    ExamChoice(id="a", text="Natural selection over many generations", correct=True),
                    ExamChoice(id="b", text="Random mutations only", correct=False),
                    ExamChoice(id="c", text="Organisms willing themselves to change", correct=False),
                ],
                tags=["evolution"],
            ),
        ],
    },

    # Data Science exams
    "data_science": {
        1: [
            ExamQuestion(
                id="ds_s1_q1",
                text="Data science typically combines:",
                choices=[
                    ExamChoice(id="a", text="Statistics, programming, domain expertise", correct=True),
                    ExamChoice(id="b", text="Guessing only", correct=False),
                    ExamChoice(id="c", text="One skill exclusively", correct=False),
                ],
                tags=["intro_ds"],
            ),
            ExamQuestion(
                id="ds_s1_q2",
                text="Exploratory Data Analysis (EDA) helps you:",
                choices=[
                    ExamChoice(id="a", text="Understand data structure, patterns, anomalies", correct=True),
                    ExamChoice(id="b", text="Skip to conclusions", correct=False),
                    ExamChoice(id="c", text="Ignore outliers", correct=False),
                ],
                tags=["eda"],
            ),
        ],
        2: [
            ExamQuestion(
                id="ds_s2_q1",
                text="Features in a dataset are:",
                choices=[
                    ExamChoice(id="a", text="Independent variables/columns used for prediction", correct=True),
                    ExamChoice(id="b", text="Only outputs", correct=False),
                    ExamChoice(id="c", text="Random data", correct=False),
                ],
                tags=["feature_engineering"],
            ),
            ExamQuestion(
                id="ds_s2_q2",
                text="Machine learning models should be evaluated using:",
                choices=[
                    ExamChoice(id="a", text="Train, validation, test splits with proper metrics", correct=True),
                    ExamChoice(id="b", text="Training data only", correct=False),
                    ExamChoice(id="c", text="Intuition", correct=False),
                ],
                tags=["model_eval"],
            ),
        ],
    },

    # Nursing exams
    "nursing": {
        1: [
            ExamQuestion(
                id="nurs_s1_q1",
                text="Patient-centered care prioritizes:",
                choices=[
                    ExamChoice(id="a", text="Individual patient values, preferences, and needs", correct=True),
                    ExamChoice(id="b", text="Only medical protocols", correct=False),
                    ExamChoice(id="c", text="Speed exclusively", correct=False),
                ],
                tags=["nursing_care"],
            ),
            ExamQuestion(
                id="nurs_s1_q2",
                text="Hand hygiene is critical in nursing because:",
                choices=[
                    ExamChoice(id="a", text="It prevents infection transmission between patients", correct=True),
                    ExamChoice(id="b", text="It's just routine", correct=False),
                    ExamChoice(id="c", text="Optional practice", correct=False),
                ],
                tags=["infection_control"],
            ),
        ],
        2: [
            ExamQuestion(
                id="nurs_s2_q1",
                text="Vital signs include:",
                choices=[
                    ExamChoice(id="a", text="Temperature, pulse, respiration, blood pressure", correct=True),
                    ExamChoice(id="b", text="Height and weight only", correct=False),
                    ExamChoice(id="c", text="Medications given", correct=False),
                ],
                tags=["assessment"],
            ),
            ExamQuestion(
                id="nurs_s2_q2",
                text="Patient safety is enhanced by:",
                choices=[
                    ExamChoice(id="a", text="Double-checking medications, proper identification, communication", correct=True),
                    ExamChoice(id="b", text="Moving quickly", correct=False),
                    ExamChoice(id="c", text="Not asking questions", correct=False),
                ],
                tags=["patient_safety"],
            ),
        ],
    },

    # Accounting exams
    "accounting": {
        1: [
            ExamQuestion(
                id="acct_s1_q1",
                text="The accounting equation is:",
                choices=[
                    ExamChoice(id="a", text="Assets = Liabilities + Equity", correct=True),
                    ExamChoice(id="b", text="Revenue = Assets", correct=False),
                    ExamChoice(id="c", text="Cash = Profit", correct=False),
                ],
                tags=["fundamentals"],
            ),
            ExamQuestion(
                id="acct_s1_q2",
                text="GAAP stands for:",
                choices=[
                    ExamChoice(id="a", text="Generally Accepted Accounting Principles", correct=True),
                    ExamChoice(id="b", text="General Asset Allocation Plan", correct=False),
                    ExamChoice(id="c", text="Gross Annual Audit Plan", correct=False),
                ],
                tags=["standards"],
            ),
        ],
        2: [
            ExamQuestion(
                id="acct_s2_q1",
                text="Debits and credits must:",
                choices=[
                    ExamChoice(id="a", text="Always balance in journal entries", correct=True),
                    ExamChoice(id="b", text="Never equal", correct=False),
                    ExamChoice(id="c", text="Be ignored", correct=False),
                ],
                tags=["journal_entry"],
            ),
            ExamQuestion(
                id="acct_s2_q2",
                text="Accrual accounting records transactions when:",
                choices=[
                    ExamChoice(id="a", text="They occur, regardless of cash flow", correct=True),
                    ExamChoice(id="b", text="Only when cash is received", correct=False),
                    ExamChoice(id="c", text="At year-end only", correct=False),
                ],
                tags=["accrual"],
            ),
        ],
    },
    # ===== ENGINEERING TRACK =====
    "eng": {
        1: [
            ExamQuestion(
                id="eng_s1_q1",
                text="What is the primary focus of engineering design?",
                choices=[
                    ExamChoice(id="a", text="Creating practical solutions to problems", correct=True),
                    ExamChoice(id="b", text="Decorating buildings", correct=False),
                    ExamChoice(id="c", text="Writing code only", correct=False),
                ],
                tags=["design"],
            ),
            ExamQuestion(
                id="eng_s1_q2",
                text="Newton's first law states that an object at rest will remain at rest unless acted upon by:",
                choices=[
                    ExamChoice(id="a", text="A net force", correct=True),
                    ExamChoice(id="b", text="Gravity", correct=False),
                    ExamChoice(id="c", text="An external observer", correct=False),
                ],
                tags=["mechanics"],
            ),
            ExamQuestion(
                id="eng_s1_q3",
                text="What does CAD stand for?",
                choices=[
                    ExamChoice(id="a", text="Computer-Aided Design", correct=True),
                    ExamChoice(id="b", text="Computer Automatic Drafting", correct=False),
                    ExamChoice(id="c", text="Computed Advanced Design", correct=False),
                ],
                tags=["design"],
            ),
        ],
        2: [
            ExamQuestion(
                id="eng_s2_q1",
                text="Electromagnetic force is strongest when:",
                choices=[
                    ExamChoice(id="a", text="Opposite charges are closest", correct=True),
                    ExamChoice(id="b", text="Similar charges are far apart", correct=False),
                    ExamChoice(id="c", text="No magnetic field exists", correct=False),
                ],
                tags=["electricity"],
            ),
            ExamQuestion(
                id="eng_s2_q2",
                text="An integral in calculus represents:",
                choices=[
                    ExamChoice(id="a", text="The area under a curve", correct=True),
                    ExamChoice(id="b", text="The slope of a line", correct=False),
                    ExamChoice(id="c", text="The distance traveled", correct=False),
                ],
                tags=["calculus"],
            ),
        ],
        3: [
            ExamQuestion(
                id="eng_s3_q1",
                text="Ohm's Law states V = I × R. What does R represent?",
                choices=[
                    ExamChoice(id="a", text="Resistance", correct=True),
                    ExamChoice(id="b", text="Reactance", correct=False),
                    ExamChoice(id="c", text="Resonance", correct=False),
                ],
                tags=["circuits"],
            ),
            ExamQuestion(
                id="eng_s3_q2",
                text="Tensile strength measures a material's ability to:",
                choices=[
                    ExamChoice(id="a", text="Resist breaking under tension", correct=True),
                    ExamChoice(id="b", text="Resist heat", correct=False),
                    ExamChoice(id="c", text="Conduct electricity", correct=False),
                ],
                tags=["materials"],
            ),
        ],
        4: [
            ExamQuestion(
                id="eng_s4_q1",
                text="The first law of thermodynamics deals with:",
                choices=[
                    ExamChoice(id="a", text="Conservation of energy", correct=True),
                    ExamChoice(id="b", text="Entropy always increases", correct=False),
                    ExamChoice(id="c", text="Heat flows from cold to hot", correct=False),
                ],
                tags=["thermodynamics"],
            ),
            ExamQuestion(
                id="eng_s4_q2",
                text="Boolean algebra uses which basic operations?",
                choices=[
                    ExamChoice(id="a", text="AND, OR, NOT", correct=True),
                    ExamChoice(id="b", text="Plus, minus, multiply", correct=False),
                    ExamChoice(id="c", text="Sine, cosine, tangent", correct=False),
                ],
                tags=["digital"],
            ),
        ],
        5: [
            ExamQuestion(
                id="eng_s5_q1",
                text="A control system's feedback loop is used to:",
                choices=[
                    ExamChoice(id="a", text="Maintain desired output by adjusting input", correct=True),
                    ExamChoice(id="b", text="Increase system complexity", correct=False),
                    ExamChoice(id="c", text="Reduce power consumption", correct=False),
                ],
                tags=["control"],
            ),
            ExamQuestion(
                id="eng_s5_q2",
                text="AC power transmission uses high voltage because:",
                choices=[
                    ExamChoice(id="a", text="To reduce resistive losses in wires", correct=True),
                    ExamChoice(id="b", text="To make electricity stronger", correct=False),
                    ExamChoice(id="c", text="DC cannot be transmitted long distances", correct=False),
                ],
                tags=["power"],
            ),
        ],
        6: [
            ExamQuestion(
                id="eng_s6_q1",
                text="What is the main advantage of solar photovoltaic systems?",
                choices=[
                    ExamChoice(id="a", text="Renewable and produce no emissions", correct=True),
                    ExamChoice(id="b", text="They work during night", correct=False),
                    ExamChoice(id="c", text="They require no maintenance", correct=False),
                ],
                tags=["renewable"],
            ),
            ExamQuestion(
                id="eng_s6_q2",
                text="Gantt charts are primarily used in project management for:",
                choices=[
                    ExamChoice(id="a", text="Scheduling and tracking tasks over time", correct=True),
                    ExamChoice(id="b", text="Calculating project costs", correct=False),
                    ExamChoice(id="c", text="Defining project scope", correct=False),
                ],
                tags=["management"],
            ),
        ],
        7: [
            ExamQuestion(
                id="eng_s7_q1",
                text="System integration testing ensures that:",
                choices=[
                    ExamChoice(id="a", text="All components work together correctly", correct=True),
                    ExamChoice(id="b", text="Individual functions are optimized", correct=False),
                    ExamChoice(id="c", text="The system costs less", correct=False),
                ],
                tags=["testing"],
            ),
            ExamQuestion(
                id="eng_s7_q2",
                text="Professional engineering ethics require engineers to:",
                choices=[
                    ExamChoice(id="a", text="Prioritize public safety and welfare", correct=True),
                    ExamChoice(id="b", text="Always maximize profit", correct=False),
                    ExamChoice(id="c", text="Avoid responsibility for failures", correct=False),
                ],
                tags=["ethics"],
            ),
        ],
        8: [
            ExamQuestion(
                id="eng_s8_q1",
                text="A capstone project integrates:",
                choices=[
                    ExamChoice(id="a", text="All major engineering disciplines and skills", correct=True),
                    ExamChoice(id="b", text="Only the latest technology", correct=False),
                    ExamChoice(id="c", text="Exclusively theoretical knowledge", correct=False),
                ],
                tags=["capstone"],
            ),
            ExamQuestion(
                id="eng_s8_q2",
                text="Preparing for the PE exam primarily requires:",
                choices=[
                    ExamChoice(id="a", text="Deep technical knowledge and professional experience", correct=True),
                    ExamChoice(id="b", text="Just computer skills", correct=False),
                    ExamChoice(id="c", text="Only passing all college exams", correct=False),
                ],
                tags=["professional"],
            ),
        ],
    },

}
