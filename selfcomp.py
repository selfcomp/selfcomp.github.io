from flask import Flask, render_template

app = Flask(__name__)

works = [
         ('GitHub', 'https://github.com/ttm'),
         ('arXiv', 'https://arxiv.org/a/fabbri_r_1.html'),
         ('Lattes', 'http://lattes.cnpq.br/1840472218825589'),
         ('Sound Cloud', 'https://soundcloud.com/le-poste-tche/')
        ]

interests = ['data audiovisualization', 'linked data', 'complex networks', 'text mining', 'computational inteligence']

selected = ['Fabbri, R., Fabbri, R., Antunes, D. C., Pisani, M. M., & de Oliveira Junior, O. N. (2017). Temporal stability in human interaction networks. Physica A: Statistical Mechanics and its Applications, 486, 92-105',
            'Vieira, V., Fabbri, R., Travieso, G., Oliveira Jr, O. N., & da Fontoura Costa, L. (2012). A quantitative approach to evolution of music and philosophy. Journal of Statistical Mechanics: Theory and Experiment, 2012(08), P08010.',
            'Fabbri, R. (2017). Topological stability and textual differentiation in human interaction networks: statistical analysis, visualization and linked data (Doctoral dissertation, Universidade de São Paulo).',
            'Fabbri, R., Junior, V. V. D. S., Pessotti, A. C. S., Corrêa, D. C., & Oliveira Jr, O. N. (2014). Musical elements in the discrete-time representation of sound. arXiv preprint arXiv:1412.6853.',
            'Half-Shape suite'
           ]


@app.route("/")
def hello():
    return render_template('child.html', title='ttm home', works=works, interests=interests, selected=selected)





